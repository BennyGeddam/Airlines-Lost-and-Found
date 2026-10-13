from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import TheLostItems
from .forms import FormForItemsLost
from django.utils import timezone
from django.urls import reverse
from .snslostitem import send_notification
from .sqslostitem import send_message_to_sqs

# home page view shows all lost items.
    # item detail page view needs login.
        # cri(crucial info) page.
            # success page.
                # reporting a lost item.
                    # updating details of a reported item condition login required.
                        # mark an item as found condtions login and POST with location.

def home(request):
    items = TheLostItems.objects.filter(found=False)
    return render(request, 'spot_items/home.html', {'items': items})

class itemdetails(LoginRequiredMixin, DetailView):
    model = TheLostItems
    context_object_name = 'item'
    template_name = 'spot_items/item_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reported_by'] = self.object.reported_by
        return context

def cri(request):
    return render(request, 'spot_items/cri.html')

def confirmationsuccessview(request):
    return render(request, 'spot_items/success.html')

@login_required
def reportlostitems(request):
    if request.method == 'POST':
        form = FormForItemsLost(request.POST, request.FILES)
        if form.is_valid():
            lost_item = form.save(commit=False)
            lost_item.reported_by = request.user
            lost_item.save()
            messages.success(request, "Item reported successfully!")
            send_notification({
                'title': lost_item.title,
                'description': lost_item.description,
                'location': lost_item.location,
                'lost_date': lost_item.lost_date
            })
            send_message_to_sqs({
                'title': lost_item.title,
                'description': lost_item.description,
                'location': lost_item.location,
                'lost_date': lost_item.lost_date
            })
            return redirect('spot_items:confirmationsuccessview')
    else:
        form = FormForItemsLost()
    return render(request, 'spot_items/report_lost_items.html', {'form': form})


@login_required
def updatelostitem(request, ItemID):
    item = get_object_or_404(TheLostItems, pk=ItemID)

    if request.method == 'POST':
        form = FormForItemsLost(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Item details are updated successfully!")
            return redirect(reverse('spot_items:detail', args=[ItemID]))
    else:
        form = FormForItemsLost(instance=item)
    return render(request, 'spot_items/update_lost_item.html', {'form': form, 'item': item})


@login_required
def markfounditem(request, ItemID):
    item = get_object_or_404(TheLostItems, pk=ItemID)
    if request.method == 'POST':
        location = request.POST.get('location', '').strip()
        if location:
            item.item_found_by = request.user
            item.found = True
            item.found_location = location
            item.found_date = timezone.now()
            item.save()
            messages.success(request, f'Item marked as found at {location}.')
        else:
            messages.error(request, 'To mark as found, location is needed.')
    return redirect('airport_staff:airport_staff_dashboard')

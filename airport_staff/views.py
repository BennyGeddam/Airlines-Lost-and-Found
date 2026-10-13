from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import Feedbacks
from .forms import FeedbackForm
from spot_items.models import TheLostItems

    # checks if a user is airport staff
        # if the user is logged in as staff member getting staff status

def checkairportstaff(user):
    return user.is_authenticated and user.is_staff

# Handles the submission of feedback
    # cannot save feedback without saving
        #getting user of feedback
            # saving feedback not yet
                # Send back to home
                    # New form

def submitfeedbacks(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            messages.success(request, "Feedback submitted successfully")
            return redirect('spot_items:home')
    else:
        form = FeedbackForm()
    return render(request, 'airport_staff/submit_feedbacks.html', {'form': form})

# special dashboard for airport staff users
  # full/complete subbmitted feedbacks as list
      # only found items as list
def airportstaffdashboard(request):
    feedbacks_list = Feedbacks.objects.all()
    founditems_list = TheLostItems.objects.filter(found=True)
    context = {
        'feedbacks_list': feedbacks_list,
        'founditems_list': founditems_list,
    }
    return render(request, 'airport_staff/airport_staff_dashboard.html', context)

# deletes a existing feedback
      # staff can only has permission
          # condition of 404
            #  it got deleted
                  # Back to  dashboard
@user_passes_test(checkairportstaff)
def feedbackdeletion(request, feedbackId):
    feedback = get_object_or_404(Feedbacks, id=feedbackId)
    feedback.delete()
    messages.success(request, "Feedback deleted successfully")
    return redirect('airport_staff:airport_staff_dashboard')

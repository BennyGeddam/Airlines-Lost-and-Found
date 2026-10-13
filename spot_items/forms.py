from django import forms
from .models import TheLostItems

# lost items form
    # fields for the form
        # custom validation 'title' field
            # Additional conditions
                # Customizing the form
class FormForItemsLost(forms.ModelForm):
    class Meta:
        model = TheLostItems
        fields = ['title', 'description', 'location', 'image', 'found', 'email']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title

    def __init__(self, *args, **kwargs):
        super(FormForItemsLost, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'required': False})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 11, 'cols': 50})
        self.fields['location'].widget.attrs.update({'class': 'form-control', 'rows': 2, 'cols': 50})
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['found'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs['placeholder'] = 'Enter the title of the item'
        self.fields['location'].widget.attrs['placeholder'] = 'Where did you lose the item?'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe the item that was lost'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address'

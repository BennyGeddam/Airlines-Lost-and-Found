from django import forms
from .models import Feedbacks

# Form for submitting feedbacks
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedbacks
        fields = ['feedback_text', 'rating']

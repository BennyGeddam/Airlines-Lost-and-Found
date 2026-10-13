from django import forms
from .models import Feedbacks

# Form for feedback sending
    # Meta class is used to specify the model and fields
class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedbacks
        fields = ['feedback_text', 'rating']

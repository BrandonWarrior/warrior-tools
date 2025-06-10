from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    """
    Form for creating and updating a Testimonial.
    """

    class Meta:
        model = Testimonial
        fields = ['content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Share your experience...',
                'class': 'form-control testimonial-content'
            }),
            'rating': forms.Select(attrs={
                'class': 'form-control testimonial-rating'
            }),
        }
        error_messages = {
            'content': {
                'required': 'A testimonial is required.'
            }
        }

    def __init__(self, *args, **kwargs):
        """
        Initialise TestimonialForm and remove the native HTML5 'required'
        attribute from widget attributes.
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.pop('required', None)

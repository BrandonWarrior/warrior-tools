"""
Forms module for the profiles app.

Defines a ModelForm for editing user profile information,
including custom placeholder text and CSS classes.
"""

from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for updating the UserProfile model.

    Excludes the user field and sets custom placeholders,
    autofocus, and styling for all form fields.
    """

    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        """
        Customize form fields by adding placeholders, CSS classes,
        removing labels, and setting autofocus on the first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "default_full_name": "Full Name",
            "default_phone_number": "Phone Number",
            "default_postcode": "Postal Code",
            "default_town_or_city": "Town or City",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_county": "County",
        }

        self.fields["default_full_name"].widget.attrs["autofocus"] = True

        for field in self.fields:
            if field != "default_country":
                placeholder = placeholders.get(field, field.replace("_", " ").title())
                if self.fields[field].required:
                    placeholder += " *"
                self.fields[field].widget.attrs["placeholder"] = placeholder

            self.fields[field].widget.attrs[
                "class"
            ] = "border-black rounded-0 profile-form-input"
            self.fields[field].label = False

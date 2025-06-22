from django import forms
from django_countries.widgets import CountrySelectWidget
from .models import Order


class AccessibleCountrySelectWidget(CountrySelectWidget):
    """
    Custom CountrySelectWidget that avoids injecting inaccessible flag images
    by rendering only the plain select HTML without added flag attributes.
    """
    template_name = 'django/forms/widgets/select.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        # Remove any custom flag attributes injected by django-countries
        for group in context.get('widget', {}).get('optgroups', []):
            for option in group[1]:
                option.get('attrs', {}).pop('data-country-flag-url', None)

        return context


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'street_address1',
            'street_address2',
            'town_or_city',
            'postcode',
            'country',
            'county',
        )
        widgets = {
            'country': AccessibleCountrySelectWidget(
                attrs={
                    'class': 'stripe-style-input',
                    'aria-label': 'Country',
                }
            ),
        }
        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'postcode': 'Postal Code',
            'county': 'County',
            'country': 'Country',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Placeholder text for form fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'postcode': 'Postal Code',
            'county': 'County',
        }

        # Autofocus on the first field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Apply placeholders, classes, and aria-labels
        for field in self.fields:
            if field != 'country':
                placeholder = (
                    f"{placeholders[field]} *"
                    if self.fields[field].required else placeholders[field]
                )
                self.fields[field].widget.attrs['placeholder'] = placeholder

            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].widget.attrs['aria-label'] = self.fields[field].label

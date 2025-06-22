"""
Custom widget for file input that provides a styled clear checkbox.

Overrides Django's ClearableFileInput to customize labels and template.
"""

from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    A ClearableFileInput widget with customised labels and template
    for improved UI in product image uploads.
    """
    clear_checkbox_label = _("Remove")
    initial_text = _("Current Image")
    input_text = _("")
    template_name = "products/custom_widget_templates/custom_clearable_file_input.html"

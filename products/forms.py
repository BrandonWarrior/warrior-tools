from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category

class ProductForm(forms.ModelForm):
    VARIANTS_WITH_SIZES = [
        'hammer',
        'sds_drill',
        'drill_driver',
        'impact_driver',
        'jigsaw',
        'circular_saw',
        'orbital_sander',
        'tape_measure',
        'hand_saw',
    ]

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

        instance = kwargs.get('instance')
        if instance and instance.variant_type not in self.VARIANTS_WITH_SIZES:
            self.initial['has_sizes'] = False

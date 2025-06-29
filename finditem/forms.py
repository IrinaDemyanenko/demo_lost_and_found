from django import forms
from finditem.models import FoundItem



class FoundItemForm(forms.ModelForm):
    """Форма заявки о потерянной вещи - на главной странице вэб-приложения."""
    class Meta:
        model = FoundItem
        fields = ['description', 'found_date', 'station', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'found_date': forms.DateInput(attrs={'type': 'date'}),
        }
        exclude = ['image_url', 'status']

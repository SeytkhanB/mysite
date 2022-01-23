
import re
from django.core.exceptions import ValidationError
from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'        # this line gives us all fields
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Наименование не должно начинаться с цифры')
        return title


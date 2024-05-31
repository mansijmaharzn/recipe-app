from django import forms

from .models import Recipe


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'steps', 'image', 'category']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'ingredients': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'steps': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
        }


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'steps', 'category']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'ingredients': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'steps': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
        }

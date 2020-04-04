from django import forms
from .models import Author

class AuthorProfForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('image', 'gender')










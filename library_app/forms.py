from library_app.models import Book_info
from django import forms
class Book_form(forms.ModelForm):
    class Meta:
        model=Book_info
        fields="__all__"
    
   
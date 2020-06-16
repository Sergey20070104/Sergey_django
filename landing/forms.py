from.models import Diary
from django import forms

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = '__all__'

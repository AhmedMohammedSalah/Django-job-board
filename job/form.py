from .models import Apply ,Job
from django import forms
class ApplyForm(forms.ModelForm):
    """Form definition for ApplyForm."""

    class Meta:
        """Meta definition for ApplyForm."""
        model = Apply
        fields = ['name','email'
        ,'website','cv','cover_letter',]
class JobForm (forms.ModelForm):
    #Metadata
    class Meta:
        model = Job
        fields = '__all__'
        exclude= ('slug','owner')


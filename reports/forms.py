from django import forms
from .models import PostReport

class ReportForm(forms.ModelForm):
    class Meta:
        model = PostReport
        fields = ['reason']
        widgets = {
            'reason': forms.Textarea(attrs={'maxlength': '300'})
        }

    def clean_reason(self):
        reason = self.cleaned_data.get('reason')
        if "http://" in reason or "https://" in reason:
            raise forms.ValidationError("Links are not allowed in the report reason.")
        return reason

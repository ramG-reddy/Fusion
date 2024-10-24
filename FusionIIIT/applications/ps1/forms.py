from applications.ps1.models import StockEntry
from django import forms


class stockforms(forms.ModelForm):
    class Meta:
        model = StockEntry
        fields = "__all__"

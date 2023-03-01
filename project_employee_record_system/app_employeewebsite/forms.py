from django import forms
from .models import Employee


class EmployeeCreateForm(forms.ModelForm):
    """ Forms Class for Employee Creation """

    class Meta:
        fields = "__all__"
        # fields = ("full_name", "contact")
        model = Employee


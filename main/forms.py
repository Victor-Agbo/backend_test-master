from django import forms
from main import models


class AddEmployee(forms.Form):
    all_employees = models.Employee.objects.all()
    show_employees = []

    for employee in all_employees:
        if not employee.company:
            show_employees.append(
                [employee.id, employee.first_name + " " + employee.last_name]
            )
    employees = forms.ChoiceField(required=True, choices=show_employees)
    employees.widget.attrs.update({"class": "form-select"})

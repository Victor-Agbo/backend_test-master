from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from main import models
from . import forms

# Create your views here.


def companies_view(request):
    companies = models.Company.objects.all()
    employees = models.Employee.objects.all()
    return render(request, "companies.html", {"companies": companies, "employees":employees})


def add_employee(request, company_id):
    company = models.Company.objects.get(id=company_id)
    if request.method == "POST":
        form = forms.AddEmployee(request.POST)
        if form.is_valid():
            employee = models.Employee.objects.get(id = form.cleaned_data["employees"])
            employee.company = company
            employee.save()
            return HttpResponseRedirect(reverse("api:companies"))
    else:
        form = forms.AddEmployee()
    return render(request, "add_employee.html", {"form": form, "company":company})

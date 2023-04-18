from django.urls import path

from main import views

app_name = "api"

urlpatterns = [
    path("", views.companies_view, name="companies"),
    path("add_employee/<int:company_id>", views.add_employee, name="add_employee"),
]

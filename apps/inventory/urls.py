from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    # Company
    path("company/list/", views.CompanyListView.as_view(), name="company-list"),
    path("company/create/", views.CompanyCreateView.as_view(), name="company-create"),
    path("company/edit/<str:cnpj>", views.CompanyEditView.as_view(), name="company-edit"),
    path("company/delete/<str:cnpj>", views.CompanyDeleteView.as_view(), name="company-delete"),

    # Employee
    path("employee/list/", views.EmployeeListView.as_view(), name="employee-list"),
    path("employee/create/", views.EmployeeCreateView.as_view(), name="employee-create"),
    path("employee/edit/<int:code>", views.EmployeeEditView.as_view(), name="employee-edit"),
    path("employee/delete/<int:code>", views.EmployeeDeleteView.as_view(), name="employee-delete"),

    # Client
    path("client/list/", views.ClientList.as_view(), name="client-list"),
    path("client/create/", views.ClientCreateView.as_view(), name="client-create"),
    path("client/edit/<str:document>", views.ClientEditView.as_view(), name="client-edit"),
    path("client/delete/<str:document>", views.ClientDeleteView.as_view(), name="client-delete"),


    # Car
    path("car/list", views.CarListView.as_view(), name="car-list")
]

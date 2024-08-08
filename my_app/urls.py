from django.urls import path
from .views import index_page,  get_max_salary_employees, get_dependendents

urlpatterns = [
    path('',index_page, name='index_page'),
    path('salary/<int:top>', get_max_salary_employees, name='employee-list'),
    path('deps/<int:employee_id>', get_dependendents, name='deps-list'),

]
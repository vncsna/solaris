from django.urls import path
from . import views

urlpatterns = [
    path('olders/<int:n>', views.get_olders, name='olders'),
    path('youngers/<int:n>', views.get_youngers, name='youngers'),
    path('gender/dist', views.get_gender_distribution, name='gender_dist'),
    path('bloodtype/freq', views.get_bloodtype_frequency, name='bloodtype_freq'),
    path('person/<str:cpf>', views.get_person_by_cpf, name='person_by_cpf'),
    path('people', views.get_people, name='people'),
    path('people/search', views.get_people_by_name, name='people_by_name'),
]
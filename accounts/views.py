from django.http import JsonResponse
from django.db.models import Count

from .models import Person

def get_olders(request, n):
    """Returns n oldest people"""
    people = Person.objects.order_by('data_nasc')[:n]
    people = people.values()
    people = list(people)
    return JsonResponse(people, safe=False)

def get_youngers(request, n):
    """Returns n youngest people"""
    people = Person.objects.order_by('-data_nasc')[:n]
    people = people.values()
    people = list(people)[::-1]
    return JsonResponse(people, safe=False)

def get_gender_distribution(request):
    """Returns the gender distribution"""
    dist = Person.gen_distribution('sexo')
    return JsonResponse(dist, safe=False)

def get_bloodtype_frequency(request):
    """Returns the blood type frequency"""
    freq = Person.gen_frequency('tipo_sanguineo')
    return JsonResponse(freq, safe=False)

def get_person_by_cpf(request, cpf):
    """Returns a person by their cpf"""
    person = Person.objects.filter(cpf=cpf)
    person = person.values()
    person = list(person)
    return JsonResponse(person, safe=False)

def get_people(request):
    """Returns people's names """
    people = Person.objects.order_by('nome')
    people = people.values_list('nome', flat=True)
    people = list(people)
    return JsonResponse(people, safe=False)

def get_people_by_name(request):
    """Returns people by their names"""
    q = request.GET.get('q', None)
    if q:
        people = Person.objects.filter(nome__icontains=q)
        people = people.values_list('nome', flat=True)
        people = list(people)
        return JsonResponse(people, safe=False)
    else:
        return JsonResponse({"error": "invalid query"})
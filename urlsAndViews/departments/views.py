from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def view_with_var(request, variable):
    return HttpResponse(f"<h1>Var: {variable}</h1>")

def view_with_pk(request, pk):
    return HttpResponse(f"<h1>Pk: {pk}</h1>")

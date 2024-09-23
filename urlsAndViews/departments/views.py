from django.http import HttpResponse
from django.shortcuts import render

from urlsAndViews.departments.models import Department


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def view_with_var(request, variable):
    # return HttpResponse(f"<h1>Var: {variable}</h1>")
    return render(request, 'departments/name_template.html', {'variable': variable})

def view_with_pk(request, pk):
    return HttpResponse(f"<h1>Pk: {pk}</h1>")


def view_with_slug(request, slug):
    department = Department.objects.get(slug=slug)
    return HttpResponse(f"<h1>The slug is: {slug}</h1>"
                        f"<h2>The name is: {department}</h2>"
                        f"<h2>The pk is: {department.pk}</h2>")


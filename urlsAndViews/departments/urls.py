from django.urls import path
from urlsAndViews.departments.views import index, view_with_var, view_with_pk

urlpatterns = [
    path('', index, name='index'),
    path('<variable>/', view_with_var, name='var'),
    path('<int:pk>/', view_with_pk, name='pk'),
]

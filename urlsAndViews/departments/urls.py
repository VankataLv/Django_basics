from django.urls import path
from urlsAndViews.departments.views import index, view_with_var, view_with_pk, view_with_slug

urlpatterns = [
    path('', index, name='index'),
    # path('<slug:slug>/', view_with_slug, name='slug'),
    path('<variable>/', view_with_var, name='var'),
    path('<int:pk>/', view_with_pk, name='pk'),

]

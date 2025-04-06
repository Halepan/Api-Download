from django.urls import path
from . import views


urlpatterns = [
    path('descargas/',views.DescargasListCreateView.as_view(),name='list-create'),
    path('descargas/<int:pk>',views.DescargasRetrieveUpdateDestroyViews.as_view(),name ='detaill-del'),
]
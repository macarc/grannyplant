from django.urls import path, include
from django.contrib import admin
from .views import PlantView, PlantCreateView, PlantEditView, AreaCreateView, WhichAreaView, SpecificAreaCreateView, PlantOrderByLocationView, PlantDeleteView

urlpatterns = [
        path('plant/new', PlantCreateView.as_view(), name='add_plant'),
        path('area/new', AreaCreateView.as_view(), name='add_area'),
        path('area/which', WhichAreaView.as_view(), name='which_area'),
        path('area/specific/new', SpecificAreaCreateView.as_view(), name='add_specific_area'),
        path('plant/<int:pk>/edit', PlantEditView.as_view(), name='edit_plant'),
        path('plant/<int:pk>/delete', PlantDeleteView.as_view(), name='delete_plant'),
        path('location', PlantOrderByLocationView.as_view(), name='order_by_location'),
        path('account/', include('django.contrib.auth.urls')),
        path('', PlantView.as_view(), name='home')
        ]

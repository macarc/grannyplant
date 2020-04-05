from django.views.generic import CreateView, ListView, UpdateView, TemplateView, DeleteView
from django.forms import ModelForm, modelformset_factory
from django.urls import reverse_lazy
from .models import Plant, Area, SpecificArea
from .widgets import LocationWidget


class NewPlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = ('latin_name','english_name','description','size','care','where')
        widgets = {'where': LocationWidget}

class PlantView(ListView):
    model = Plant
    template_name = 'index.html'
    context_object_name = 'all_plants'

    def get_queryset(self):
        order=self.request.GET.get('orderby','latin_name')
        return Plant.objects.order_by(order)

class PlantOrderByLocationView(ListView):
    model = Area
    template_name = 'location.html'
    context_object_name = 'all_areas'

    class Meta:
        ordering = ['name', 'specific_area__name', 'specific_area__plant__latin_name']

class PlantCreateView(CreateView):
    form_class = NewPlantForm
    template_name = 'new.html'
    new_what = 'Plant'

class PlantEditView(UpdateView):
    model = Plant
    template_name = 'edit.html'
    fields = ['latin_name','english_name','description','size','care','where']

class PlantDeleteView(DeleteView):
    model = Plant
    template_name = 'delete_plant.html'
    success_url = reverse_lazy('home')

class WhichAreaView(TemplateView):
    template_name = 'whicharea.html'

class AreaCreateView(CreateView):
    model = Area
    template_name = 'new.html'
    fields = ['name']
    new_what = 'General Area'

class SpecificAreaCreateView(CreateView):
    model = SpecificArea
    template_name = 'new.html'
    fields = ['name','general_area']
    new_what = 'Specific Area'

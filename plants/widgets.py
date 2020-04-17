from django.forms.widgets import Widget
from django.template import loader
from django.utils.safestring import mark_safe
from .models import Area, SpecificArea

class LocationWidget(Widget):
    template_name = 'location_widget.html'

    def get_context(self,name,value,attrs, renderer):
        return {'widget': {
            'name': name,
            'values':value,
            'id': attrs['id'],
            'general_areas': Area.objects.order_by('name'),
            'required': attrs['required']
            }}

    def value_from_datadict(self,data,files,name):
        raw = data.getlist(name)
        new = []
        for val in raw:
            id_ = int(val)
            new.append(SpecificArea.objects.get(pk=id_))
        return new

    def render(self,name,value,attrs, renderer, *args, **kwargs):
        context = self.get_context(name, value, attrs, renderer)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)

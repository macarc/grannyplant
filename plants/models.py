from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from gettext import gettext as _

class Plant(models.Model):
    latin_name = models.CharField(max_length=100,blank=True,null=True)
    english_name = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    size = models.CharField(max_length=100,blank=True,null=True)
    care = models.TextField(blank=True,null=True)
    where = models.ManyToManyField(
            'SpecificArea',
            related_name='plants',
            related_query_name='plant',
            )


    def __str__(self):
        if self.latin_name:
            return self.latin_name
        else:
            return self.english_name

    def clean(self):
        if not self.latin_name and not self.english_name:
            raise ValidationError({'latin_name': _('Either Latin name or English name should have a value')})

    def get_absolute_url(self):
        return reverse('add_plant')

class Area(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('add_area')


class SpecificArea(models.Model):
    name = models.CharField(max_length=100)
    general_area = models.ForeignKey(
            'Area',
            on_delete=models.CASCADE,
            related_name='specific_areas',
            related_query_name='specific_area',
            )
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('add_specific_area')


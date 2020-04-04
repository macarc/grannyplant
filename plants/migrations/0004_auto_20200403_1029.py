# Generated by Django 2.1 on 2020-04-03 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_plant_where'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specificarea',
            name='general_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specific_areas', related_query_name='specific_area', to='plants.Area'),
        ),
    ]
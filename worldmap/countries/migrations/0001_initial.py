# Generated by Django 3.2.4 on 2021-06-08 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countrydata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('geojson', models.CharField(max_length=128)),
                ('added_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]

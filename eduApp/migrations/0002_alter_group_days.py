# Generated by Django 3.2.7 on 2021-09-20 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='days',
            field=models.ManyToManyField(related_name='groups', to='eduApp.Day'),
        ),
    ]

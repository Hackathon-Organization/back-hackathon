# Generated by Django 5.0 on 2023-12-06 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelagem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projetos',
            name='tecnologia',
        ),
    ]

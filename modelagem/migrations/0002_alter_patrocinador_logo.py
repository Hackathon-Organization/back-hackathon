# Generated by Django 4.2.7 on 2023-11-24 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("uploader", "0001_initial"),
        ("modelagem", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patrocinador",
            name="logo",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]
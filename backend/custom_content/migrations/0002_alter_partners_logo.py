# Generated by Django 4.0.3 on 2022-03-17 20:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("custom_content", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="partners",
            name="logo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="partners/",
                verbose_name="Logo",
            ),
        ),
    ]

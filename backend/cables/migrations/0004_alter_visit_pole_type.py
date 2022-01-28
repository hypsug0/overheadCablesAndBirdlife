# Generated by Django 4.0.1 on 2022-01-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cables", "0003_remove_visit_visit_visit_remark"),
    ]

    operations = [
        migrations.AlterField(
            model_name="visit",
            name="pole_type",
            field=models.ManyToManyField(
                help_text="Type of pole attached with this visit",
                related_name="visit_poletype",
                to="cables.PoleType",
                verbose_name="Type of pole attached with this visit",
            ),
        ),
    ]

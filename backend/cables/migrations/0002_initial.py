# Generated by Django 4.0.1 on 2022-01-18 11:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cables", "0001_initial"),
        ("media", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sensitive_area", "0001_initial"),
        ("sinp_nomenclatures", "0002_alter_source_unique_together"),
        ("geo_area", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="segment",
            name="geo_area",
            field=models.ManyToManyField(
                blank=True,
                help_text="Associated Administrative and Natural Areas",
                related_name="%(app_label)s_%(class)s_geo_area",
                to="geo_area.GeoArea",
                verbose_name="Associated Administrative and Natural Areas",
            ),
        ),
        migrations.AddField(
            model_name="segment",
            name="sensitivity_areas",
            field=models.ManyToManyField(
                blank=True,
                help_text="Associated Sensitivity Areas",
                related_name="%(app_label)s_%(class)s_sensitive_area",
                to="sensitive_area.SensitiveArea",
                verbose_name="Associated Sensitivity Areas",
            ),
        ),
        migrations.AddField(
            model_name="segment",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="pole",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="pole",
            name="geo_area",
            field=models.ManyToManyField(
                blank=True,
                help_text="Associated Administrative and Natural Areas",
                related_name="%(app_label)s_%(class)s_geo_area",
                to="geo_area.GeoArea",
                verbose_name="Associated Administrative and Natural Areas",
            ),
        ),
        migrations.AddField(
            model_name="pole",
            name="sensitivity_areas",
            field=models.ManyToManyField(
                blank=True,
                help_text="Associated Sensitivity Areas",
                related_name="%(app_label)s_%(class)s_sensitive_area",
                to="sensitive_area.SensitiveArea",
                verbose_name="Associated Sensitivity Areas",
            ),
        ),
        migrations.AddField(
            model_name="pole",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="equipment",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="equipment",
            name="media",
            field=models.ManyToManyField(
                blank=True,
                editable=False,
                help_text="Media attached with this equipment",
                related_name="equipment_media",
                to="media.Media",
                verbose_name="Media attached with this equipment",
            ),
        ),
        migrations.AddField(
            model_name="equipment",
            name="pole",
            field=models.ForeignKey(
                blank=True,
                help_text="Pole the equipment is installed on",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="equipment_pole",
                to="cables.pole",
                verbose_name="Pole the equipment is installed on",
            ),
        ),
        migrations.AddField(
            model_name="equipment",
            name="pole_eqmt_type",
            field=models.ForeignKey(
                blank=True,
                help_text="Type of equipment for pole",
                limit_choices_to={"type__mnemonic": "pole_equipment"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="equipment_pole_eqmt_type",
                to="sinp_nomenclatures.item",
                verbose_name="Type of equipment for pole",
            ),
        ),
        migrations.AddField(
            model_name="equipment",
            name="segment",
            field=models.ForeignKey(
                blank=True,
                help_text="Segment the equipment is installed on",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="equipment_segment",
                to="cables.segment",
                verbose_name="Segment the equipment is installed on",
            ),
        ),
        migrations.AddField(
            model_name="equipment",
            name="sgmt_eqmt_type",
            field=models.ForeignKey(
                blank=True,
                help_text="Type of equipment for segment",
                limit_choices_to={"type__mnemonic": "pole_equipment"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="equipment_sgmt_eqmt_type",
                to="sinp_nomenclatures.item",
                verbose_name="Type of equipment for segment",
            ),
        ),
        migrations.AddField(
            model_name="equipment",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddConstraint(
            model_name="visit",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ("pole__isnull", False), ("segment__isnull", True)
                    ),
                    models.Q(
                        ("pole__isnull", True), ("segment__isnull", False)
                    ),
                    _connector="OR",
                ),
                name="cables_visit_only_one_of_both_field_not_null_constraint",
            ),
        ),
        migrations.AddConstraint(
            model_name="equipment",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ("pole__isnull", False), ("segment__isnull", True)
                    ),
                    models.Q(
                        ("pole__isnull", True), ("segment__isnull", False)
                    ),
                    _connector="OR",
                ),
                name="cables_equipment_only_one_infrastructure_constraint",
            ),
        ),
        migrations.AddConstraint(
            model_name="equipment",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ("pole_eqmt_type__isnull", False),
                        ("sgmt_eqmt_type__isnull", True),
                    ),
                    models.Q(
                        ("pole_eqmt_type__isnull", True),
                        ("sgmt_eqmt_type__isnull", False),
                    ),
                    _connector="OR",
                ),
                name="cables_equipment_only_type_of_infrastructure_equipment_constraint",
            ),
        ),
    ]

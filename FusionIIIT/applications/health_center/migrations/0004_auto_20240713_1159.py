# Generated by Django 3.1.5 on 2024-07-13 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("health_center", "0003_all_medicine_threshold"),
    ]

    operations = [
        migrations.AddField(
            model_name="all_prescribed_medicine",
            name="stock",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to="health_center.present_stock",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="present_stock",
            name="Expiry_date",
            field=models.DateField(default="2024-04-12"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="present_stock",
            name="medicine_id",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to="health_center.all_medicine",
            ),
            preserve_default=False,
        ),
    ]

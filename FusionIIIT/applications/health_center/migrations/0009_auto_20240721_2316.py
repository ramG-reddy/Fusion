# Generated by Django 3.1.5 on 2024-07-21 23:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("health_center", "0008_required_medicine"),
    ]

    operations = [
        migrations.RenameField(
            model_name="all_prescribed_medicine",
            old_name="revoked_priscription",
            new_name="revoked_prescription",
        ),
    ]

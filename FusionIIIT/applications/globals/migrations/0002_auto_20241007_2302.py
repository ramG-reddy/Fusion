# Generated by Django 3.1.5 on 2024-10-07 23:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("globals", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ModuleAccess",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("designation", models.CharField(max_length=155)),
                ("program_and_curriculum", models.BooleanField(default=False)),
                ("course_registration", models.BooleanField(default=False)),
                ("course_management", models.BooleanField(default=False)),
                ("other_academics", models.BooleanField(default=False)),
                ("spacs", models.BooleanField(default=False)),
                ("department", models.BooleanField(default=False)),
                ("examinations", models.BooleanField(default=False)),
                ("hr", models.BooleanField(default=False)),
                ("iwd", models.BooleanField(default=False)),
                ("complaint_management", models.BooleanField(default=False)),
                ("fts", models.BooleanField(default=False)),
                ("purchase_and_store", models.BooleanField(default=False)),
                ("rspc", models.BooleanField(default=False)),
                ("hostel_management", models.BooleanField(default=False)),
                ("mess_management", models.BooleanField(default=False)),
                ("gymkhana", models.BooleanField(default=False)),
                ("placement_cell", models.BooleanField(default=False)),
                ("visitor_hostel", models.BooleanField(default=False)),
                ("phc", models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name="extrainfo",
            name="last_selected_role",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

# Generated by Django 3.1.5 on 2024-08-13 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_procedures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_allocations',
            name='start_date',
            field=models.DateField(default=datetime.date(2024, 8, 13)),
        ),
    ]

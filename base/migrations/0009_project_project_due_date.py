# Generated by Django 3.2.5 on 2021-10-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20211019_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

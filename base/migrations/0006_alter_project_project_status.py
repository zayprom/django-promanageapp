# Generated by Django 3.2.5 on 2021-10-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20211019_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(blank=True, choices=[(1, 'pending'), (2, 'active'), (3, 'waiting'), (3, 'finished')], max_length=200, null=True),
        ),
    ]

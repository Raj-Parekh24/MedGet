# Generated by Django 3.1.4 on 2021-02-27 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mg', '0003_doctor_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

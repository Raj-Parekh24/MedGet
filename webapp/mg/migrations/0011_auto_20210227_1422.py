# Generated by Django 3.1.4 on 2021-02-27 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mg', '0010_auto_20210227_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='name',
        ),
        migrations.AddField(
            model_name='doctor',
            name='social',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='social', to='socialaccount.socialaccount'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='usr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL),
        ),
    ]

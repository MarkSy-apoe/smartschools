# Generated by Django 4.2.4 on 2024-01-28 18:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_school_principal_principalprofile_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='commissionerprofile',
            name='state',
            field=models.CharField(choices=[('lagos', 'Lagos'), ('abuja', 'Abuja')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='has_principal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='school',
            name='joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date joined'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='state',
            field=models.CharField(choices=[('lagos', 'Lagos'), ('abuja', 'Abuja')], max_length=30, null=True),
        ),
    ]

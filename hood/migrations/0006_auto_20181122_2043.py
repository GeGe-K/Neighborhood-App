# Generated by Django 2.0 on 2018-11-22 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0005_auto_20181122_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.Neighborhood'),
        ),
    ]

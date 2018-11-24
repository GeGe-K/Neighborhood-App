# Generated by Django 2.0 on 2018-11-23 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0007_remove_neighborhood_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contacts', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('neighborhood_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.Neighborhood')),
            ],
        ),
    ]

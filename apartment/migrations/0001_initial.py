# Generated by Django 3.2.18 on 2023-03-04 00:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('amenities', models.CharField(max_length=300)),
                ('specifications', models.TextField()),
                ('address', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('UNDER_CONSTRUCTION', 'Underconstruction project'), ('READY_TO_MOVE', 'Ready to move project'), ('COMPLETED_REAL_ESTATE', 'Completed real estate project'), ('COMMERCIAL', 'Commercial')], default='UNDER_CONSTRUCTION', max_length=100)),
                ('booking_status', models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], max_length=10)),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]

# Generated by Django 3.2.3 on 2021-05-30 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_from', models.CharField(max_length=255)),
                ('city_to', models.CharField(max_length=255)),
                ('price', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TicketOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.ticket')),
            ],
        ),
    ]

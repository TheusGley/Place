# Generated by Django 5.0.1 on 2024-03-01 19:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_alter_servicos_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Agenda',
            new_name='Agendamento',
        ),
        migrations.RenameModel(
            old_name='Servicos',
            new_name='Servico',
        ),
    ]

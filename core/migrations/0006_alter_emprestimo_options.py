# Generated by Django 4.1 on 2022-09-04 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_emprestimo_status_alter_leitor_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emprestimo',
            options={'verbose_name': 'Empréstimo', 'verbose_name_plural': 'Empréstimos'},
        ),
    ]

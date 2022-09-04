# Generated by Django 4.1 on 2022-09-04 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_emprestimo_status_alter_leitor_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='status',
            field=models.BooleanField(choices=[(True, 'Em andamento'), (False, 'Finalizado')], default='Em andamento', max_length=12, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='leitor',
            name='status',
            field=models.BooleanField(choices=[(True, 'Desbloqueado'), (False, 'Bloqueado')], default='Desbloqueado', max_length=12, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='status',
            field=models.BooleanField(choices=[(True, 'Disponível'), (False, 'Indisponível')], default='Disponível', max_length=12, verbose_name='Status'),
        ),
    ]
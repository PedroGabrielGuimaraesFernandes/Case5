# Generated by Django 5.1.2 on 2024-10-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_case', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('materia', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('prazo', models.DateField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]

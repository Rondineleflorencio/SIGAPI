# Generated by Django 4.1 on 2022-09-25 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('SIGAPI_rest', '0002_aluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Egresso',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Egresso', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('matricula', models.IntegerField(unique=True)),
                ('endereco', models.CharField(max_length=120)),
                ('born', models.DateField()),
                ('cpf', models.IntegerField()),
                ('nome_pai', models.CharField(max_length=120)),
                ('nome_mae', models.CharField(max_length=120)),
                ('sexo', models.CharField(max_length=1)),
                ('telefone', models.CharField(max_length=15)),
                ('estado_civil', models.CharField(choices=[('C', 'casado'), ('S', 'solteiro')], max_length=120)),
                ('rg', models.CharField(max_length=10)),
            ],
        ),
    ]

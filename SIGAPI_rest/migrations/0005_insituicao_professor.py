# Generated by Django 4.1 on 2022-09-25 23:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('SIGAPI_rest', '0004_pais_aluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='insituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Professor', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.IntegerField(unique=True)),
                ('born', models.DateField(verbose_name=str)),
                ('endereco', models.CharField(max_length=50)),
                ('salario', models.FloatField()),
                ('grau', models.CharField(choices=[('B', 'Bacharelado'), ('L', 'Licenciatura'), ('T', 'Tecnólogo')], max_length=15)),
            ],
        ),
    ]
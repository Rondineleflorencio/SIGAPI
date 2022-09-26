# Generated by Django 4.1 on 2022-09-26 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SIGAPI_rest', '0005_insituicao_professor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('qtd_horas', models.TimeField()),
                ('semestre', models.IntegerField()),
                ('pre_requisito', models.CharField(max_length=90)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='professor', to='SIGAPI_rest.professor')),
            ],
        ),
    ]
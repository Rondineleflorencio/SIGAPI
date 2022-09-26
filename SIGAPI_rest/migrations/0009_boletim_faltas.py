# Generated by Django 4.1 on 2022-09-26 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SIGAPI_rest', '0008_alter_disciplina_qtd_horas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boletim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('C', 'CURSANDO'), ('A', 'APROVADO'), ('R', 'REPROVADO')], max_length=9)),
                ('aluno', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='aluno', to='SIGAPI_rest.aluno')),
                ('disciplinas', models.ManyToManyField(to='SIGAPI_rest.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Faltas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('isPresente', models.BooleanField(default=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='FaltasDele', to='SIGAPI_rest.aluno')),
                ('botelim', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='boletim', to='SIGAPI_rest.boletim')),
            ],
        ),
    ]
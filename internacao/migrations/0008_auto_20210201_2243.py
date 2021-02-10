# Generated by Django 3.1.5 on 2021-02-01 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internacao', '0007_auto_20201223_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boletim_Medico_Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_evolucao', models.DateTimeField()),
                ('liberacao', models.DateTimeField()),
                ('motivo', models.TextField()),
                ('status', models.TextField()),
                ('respiracao', models.TextField()),
                ('febre', models.TextField()),
                ('antibiotico', models.TextField()),
                ('pressao_arterial', models.TextField()),
                ('alimentacao', models.TextField()),
                ('urina', models.TextField()),
                ('evacuacao', models.TextField()),
                ('estado_clinico', models.TextField()),
                ('previsao_alta', models.TextField()),
                ('observacao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Internacao_Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateTimeField()),
                ('previsao_alta', models.DateTimeField()),
                ('alta', models.DateTimeField()),
                ('leito', models.TextField()),
                ('ala', models.TextField()),
                ('medico', models.TextField(blank=True, null=True)),
                ('dieta', models.TextField(blank=True, null=True)),
                ('situacao', models.TextField(blank=True, null=True)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('cor', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['ala', 'leito'],
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
                ('data_nascimento', models.DateTimeField()),
                ('convenio', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Internacao_Painel',
        ),
        migrations.AddField(
            model_name='internacao_paciente',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='internacao.paciente'),
        ),
        migrations.AddField(
            model_name='boletim_medico_paciente',
            name='internacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='internacao.internacao_paciente'),
        ),
        migrations.AddField(
            model_name='boletim_medico_paciente',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='internacao.paciente'),
        ),
    ]

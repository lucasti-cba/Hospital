# Generated by Django 3.1.2 on 2020-12-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internacao', '0005_auto_20201130_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internacao_painel',
            name='nome',
            field=models.TextField(),
        ),
    ]

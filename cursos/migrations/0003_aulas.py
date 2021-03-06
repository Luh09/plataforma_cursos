# Generated by Django 3.2.8 on 2021-10-08 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_delete_aulas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aulas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('aula', models.FileField(upload_to='aulas')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cursos.cursos')),
            ],
        ),
    ]

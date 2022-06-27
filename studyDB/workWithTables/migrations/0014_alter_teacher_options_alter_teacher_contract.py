# Generated by Django 4.0.5 on 2022-06-21 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workWithTables', '0013_alter_teacher_contract'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Преподаватель', 'verbose_name_plural': 'Таблица преподавателей'},
        ),
        migrations.AlterField(
            model_name='teacher',
            name='contract',
            field=models.OneToOneField(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='get_teacher', to='workWithTables.contract', verbose_name='Номер договора'),
        ),
    ]

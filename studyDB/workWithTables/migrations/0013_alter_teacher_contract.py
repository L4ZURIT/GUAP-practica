# Generated by Django 4.0.5 on 2022-06-15 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workWithTables', '0012_alter_teacher_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='contract',
            field=models.OneToOneField(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workWithTables.contract', verbose_name='Номер договора'),
        ),
    ]

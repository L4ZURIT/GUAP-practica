# Generated by Django 4.0.5 on 2022-06-08 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workWithTables', '0004_rename_academic_degree_id_education_academic_degree_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('date', models.CharField(max_length=15, null=True, verbose_name='Дата договора')),
                ('end_date', models.CharField(max_length=15, null=True, verbose_name='Дата расторжения')),
                ('wage_rate', models.CharField(max_length=50, null=True, verbose_name='Ставка')),
                ('notes', models.TextField(max_length=60, null=True, verbose_name='Примечания')),
            ],
            options={
                'verbose_name': 'Договор',
                'verbose_name_plural': 'Таблица договоров',
            },
        ),
        migrations.RemoveField(
            model_name='education',
            name='academic_degree',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='contract_date',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='contract_number',
        ),
        migrations.AddField(
            model_name='workload',
            name='timing',
            field=models.CharField(max_length=10, null=True, verbose_name='Распределение'),
        ),
        migrations.AlterField(
            model_name='education',
            name='diploma_data',
            field=models.TextField(max_length=60, null=True, verbose_name='Данные диплома'),
        ),
        migrations.AlterField(
            model_name='education',
            name='edu_type',
            field=models.CharField(max_length=60, verbose_name='Тип образования'),
        ),
        migrations.AlterField(
            model_name='education',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workWithTables.teacher', verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='INIPA',
            field=models.CharField(max_length=20, null=True, verbose_name='СНИЛС'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='TIN',
            field=models.CharField(max_length=20, null=True, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='academic_degree',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workWithTables.academicdegree', verbose_name='Ученая степень'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='birthday_place',
            field=models.CharField(max_length=255, null=True, verbose_name='Место рождения'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='cur_place',
            field=models.CharField(max_length=255, null=True, verbose_name='Адрес проживания'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='fluor_date',
            field=models.CharField(max_length=150, null=True, verbose_name='Дата флюорографии'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='passport',
            field=models.CharField(max_length=20, null=True, verbose_name='Паспорт'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(max_length=14, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='registration_place',
            field=models.CharField(max_length=255, null=True, verbose_name='Адрес прописки'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='second_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='workload',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workWithTables.lesson', verbose_name='Занятие'),
        ),
        migrations.AlterField(
            model_name='workload',
            name='study',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workWithTables.discipline', verbose_name='Дисциплина'),
        ),
        migrations.AlterField(
            model_name='workload',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workWithTables.teacher', verbose_name='Преподаватель'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='contract',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='workWithTables.contract', verbose_name='Номер договора'),
        ),
    ]
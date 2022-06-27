from tabnanny import verbose
from django.db import models

class AcademicRank(models.Model):
    name = models.CharField(
        verbose_name="Ученое звание",
        max_length=100,
        unique=True)
    
    class Meta:
        verbose_name = 'Ученое звание'
        verbose_name_plural = 'Таблица ученых званий'
    
    def __str__(self):
        return str(self.name)

class AcademicDegree(models.Model):
    name = models.CharField(
        verbose_name="Ученая степень",
        max_length=100,
        unique=True)
    
    class Meta:
        verbose_name = 'Ученая степень'
        verbose_name_plural = 'Таблица ученых степеней'
    
    def __str__(self):
        return str(self.name)

class Contract(models.Model):
    number = models.IntegerField(primary_key=True, unique=True)
    date = models.CharField(verbose_name="Дата договора", max_length=15, null=True)
    end_date = models.CharField(verbose_name="Дата расторжения", max_length=15, null=True)
    wage_rate = models.CharField(verbose_name="Ставка", max_length=50, null=True)
    notes = models.TextField(verbose_name="Примечания", max_length=60, null=True)

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Таблица договоров'
    
    def __str__(self):
        return '№' + str(self.number) + ', от: ' + str(self.date) + ', до: ' + str(self.end_date) + ', ставка: ' + str(self.wage_rate)

# Create your models here.
class Teacher(models.Model):
    surname = models.CharField(verbose_name="Фамилия", max_length=50)
    name = models.CharField(verbose_name="Имя", max_length=50, null=True)
    second_name = models.CharField(verbose_name="Отчество", max_length=50, null=True)
    birthday_date = models.CharField(verbose_name="Дата рождения", max_length=15, null=True)
    birthday_place = models.CharField(verbose_name="Место рождения", max_length=255, null=True)
    registration_place = models.CharField(verbose_name="Адрес прописки", max_length=255, null=True)
    cur_place = models.CharField(verbose_name="Адрес проживания", max_length=255, null=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=14, null=True)
    passport = models.CharField(verbose_name="Паспорт", max_length=20, null=True)
    TIN = models.CharField(verbose_name="ИНН", max_length=20, null=True)
    INIPA = models.CharField(verbose_name="СНИЛС", max_length=20, null=True)
    job = models.CharField(verbose_name="Должность", max_length=20, null=True)
    academic_degree = models.ManyToManyField(verbose_name="Ученая степень", to=AcademicDegree, related_name='get_teacher')
    academic_rank = models.ManyToManyField(verbose_name="Ученое звание", to=AcademicRank, related_name='get_teacher')
    contract = models.OneToOneField(verbose_name="Номер договора", to=Contract, on_delete=models.SET_NULL, max_length=50, null=True, unique=True, related_name='get_teacher')
    fluor_date = models.CharField(verbose_name="Дата флюорографии", max_length=150, null=True)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Таблица преподавателей'
    
    def get_absolute_url(self):
        return reversed('teacher', kwargs={"pk": self.pk})
    
    def __str__(self):
        return str(self.surname)

    def get_academic_degree(self):
        return "\n".join([str(p) for p in self.academic_degree.all()])

    def get_academic_rank(self):
        return "\n".join([str(p) for p in self.academic_rank.all()])


class Lesson(models.Model):
    name = models.CharField(
        verbose_name="Наименование занятия",
        max_length=100,
        unique=True)
    
    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Таблица занятий'
    
    def __str__(self):
        return str(self.name)

class Discipline(models.Model):
    name = models.CharField(
        verbose_name="Наименование дисциплины",
        max_length=100,
        unique=True)
    
    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Таблица дисциплин'

    def __str__(self):
        return str(self.name)

class WorkLoad(models.Model):
    teacher = models.ForeignKey(verbose_name="Преподаватель", to=Teacher, on_delete=models.SET_NULL, null=True, related_name="get_teachers")
    group_name = models.CharField(verbose_name="Номер группы", max_length=10)
    lesson = models.ForeignKey(verbose_name="Занятие", to=Lesson, on_delete=models.SET_NULL, null=True)
    study = models.ForeignKey(verbose_name="Дисциплина", to=Discipline, on_delete=models.SET_NULL, null=True)
    hours_type = models.CharField(verbose_name="Тип предмета", max_length=10)
    hours = models.CharField(verbose_name="Часы", max_length=10)
    hours_total = models.CharField(verbose_name="Общие часы", max_length=10)
    timing = models.CharField(verbose_name="Распределение", max_length=10, null=True)
    semester = models.CharField(verbose_name="Семестр", max_length=10)
    year = models.CharField(verbose_name="Год", max_length=4)

    class Meta:
        verbose_name = 'Нагрузка'
        verbose_name_plural = 'Таблица нагрузки'
        ordering = ['teacher']
    
    def get_absolute_url(self):
        return reversed('workload', kwargs={"id": self.pk})

    def __str__(self):
        return str(
            str(self.teacher) + ' '
            + self.group_name + ' '
            + str(self.lesson) + ' '
            + str(self.study) + ' '
            + self.timing + ' '
            + self.hours_type + ' '
            + self.hours + ' '
            + self.hours_total + ' '
            + self.semester + ' '
            + self.year)

class Education(models.Model):
    teacher = models.ForeignKey(verbose_name="Преподаватель", to=Teacher, on_delete=models.SET_NULL, null=True, related_name="get_education")
    university = models.CharField(verbose_name="Наименование учебного заведения", max_length=60)
    edu_type = models.CharField(verbose_name="Тип образования", max_length=60)
    specialization = models.CharField(verbose_name="Специальность", max_length=60)
    diploma_data = models.TextField(verbose_name="Данные диплома", max_length=60, null=True)

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Таблица образований'

    def __str__(self):
        return str(
            'Университет: ' + self.university + ', Тип образования: '
            + self.edu_type + ', Специализация: '
            + self.specialization + ', Данные диплома: '
            + self.diploma_data
        )

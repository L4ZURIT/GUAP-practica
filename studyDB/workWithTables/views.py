from django.shortcuts import render
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import TeacherSearchForm, WorkLoadSearchForm
import pandas as pd
from docxtpl import DocxTemplate
from django.core.paginator import Paginator

# Create your views here.
# login
def login(request):
    return render(
        request=request,
        template_name='workWithTables/login.html',
        context={'title': "Логин"}
        )

class WorkLoadView(View):
    form = WorkLoadSearchForm
    workLoad = WorkLoad
    template_name = 'workWithTables/tableW.html'

    def get(self, request, *args, **kwargs):
        work_load = self.workLoad.objects.all()
        paginator = Paginator(work_load, 20)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        return render(request=request, template_name=self.template_name, 
            context= {'form': self.form(), 'title': 'Таблица нарузки', 'page_obj': page_obj,})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        work_load = ''
        if form.is_valid():
            search_f = str(request.POST['search_choice'])
            search_v = str(request.POST['search_input'])
            if search_f == 'teacher':
                work_load = self.workLoad.objects.filter(teacher__surname__contains=search_v)
            elif search_f == 'group_name':
                work_load = self.workLoad.objects.filter(group_name__contains=search_v)    
            elif search_f == 'lesson':
                work_load = self.workLoad.objects.filter(lesson__name__contains=search_v)
            elif search_f == 'study':
                work_load = self.workLoad.objects.filter(study__name__contains=search_v)
            elif search_f == 'hours':
                work_load = self.workLoad.objects.filter(hours__contains=search_v)
            elif search_f == 'hours_total':
                work_load = self.workLoad.objects.filter(hours_total__contains=search_v)
            elif search_f == 'year':
                work_load = self.workLoad.objects.filter(year__contains=search_v)
            paginator = Paginator(work_load, 20)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request=request, template_name=self.template_name, 
                context= {'form': form, 'title': 'Таблица нарузки', 'page_obj': page_obj,})
        work_load = self.workLoad.objects.all()
        paginator = Paginator(work_load, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request=request, template_name=self.template_name, 
            context= {'form': form, 'title': 'Таблица нагрузки', 'page_obj': page_obj,})

class TeachersView(View):
    form = TeacherSearchForm
    teacher = Teacher
    template_name = 'workWithTables/tableT.html'

    def get(self, request, *args, **kwargs):
        teacher = self.teacher.objects.all()
        paginator = Paginator(teacher, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            request=request,
            template_name=self.template_name, 
            context= {'form': self.form(),
            'title': 'Таблица преподавателей',
            'page_obj': page_obj })

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        teacher = ''
        if form.is_valid():
            search_f = str(request.POST['search_choice'])
            search_v = str(request.POST['search_input'])
            if search_f == 'surname':
                teacher = self.teacher.objects.filter(surname__contains=search_v)
            elif search_f == 'birthday_date':
                teacher = self.teacher.objects.filter(birthday_date__contains=search_v)    
            elif search_f == 'job':
                teacher = self.teacher.objects.filter(job__contains=search_v)
            elif search_f == 'academic_degree':
                teacher = self.teacher.objects.filter(academic_degree__name__contains=search_v)
            elif search_f == 'academic_rank':
                teacher = self.teacher.objects.filter(academic_rank__name__contains=search_v)
            elif search_f == 'contract__end_date':
                teacher = self.teacher.objects.filter(contract__end_date__contains=search_v)
            paginator = Paginator(teacher, 20)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request=request, template_name=self.template_name, 
                context= {'form': form, 'title': 'Таблица преподавателей','page_obj': page_obj })
        paginator = Paginator(teacher, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        teacher = self.teacher.objects.all()
        return render(request=request,
            template_name=self.template_name, 
            context= {'form': form,
            'title': 'Таблица преподавателей',
            'page_obj': page_obj })
  
# card for one teacher from table/2
class TeacherView(DetailView):
    model = Teacher
    template_name = 'workWithTables/teacher_card.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Карточка преподавателя'
        try:
            edu = Education.objects.get(teacher=context['teacher'])
        except:
            edu = 'Не найдено'
        context['education'] = str(edu)

        return context
# form to export teacher data to a *.docx template file
def export_to_docx(request, pk):
    doc = DocxTemplate("Документ.docx")
    teacher = Teacher.objects.get(pk=pk)
    try:
        contract_date = teacher.contract.date
    except:
        contract_date = "None None None"
    try:
        contract_number = teacher.contract.number
    except:
        contract_number = "None"
    context = {
        'name': str(teacher.surname) + ' ' + str(teacher.name) + ' ' + str(teacher.second_name),
        'birth': str(teacher.birthday_date) + ' ' + str(teacher.birthday_place),
        'phone': str(teacher.phone_number), 'passport': str(teacher.passport), 'TIN': str(teacher.TIN),
        'date_d': str(contract_date).split()[0], 'date_m': str(contract_date).split()[1],
        'date_y': str(contract_date).split()[2], 'INIPA': str(teacher.INIPA),
        'contract_n': str(contract_number), 'vocation': str(teacher.job)
    }

    doc.render(context)
    doc.save(str(teacher.surname) + '.docx')

    res = f'Загружено в файл {teacher.surname}.docx'

    return render(
        request=request,
        template_name='workWithTables/export.html',
        context= { 'res': res, 'teacher_pk': pk }
    )

# home page func
def index(request):
    return render(
        request=request, 
        template_name='workWithTables/index.html', 
        context={
            'title': 'Главная страница',
        })

# load csv page func from "home"/load
def loadTable(request):
    form = False
    if request.method == "POST":
        table_teacher = pd.read_excel("Нагрузка_общая.xls")
        for i, row in table_teacher.groupby(['ФИО'])['ФИО'].count().iteritems():
            surname = str(i).split(' ')[0]
            Teacher.objects.get_or_create(surname=surname)
        for i, row in table_teacher.iterrows():
            surname = str(row['ФИО']).split(' ')[0]
            lesson, created_l = Lesson.objects.get_or_create(name=row["вид занятия"])
            study, created_st = Discipline.objects.get_or_create(name=row["дисциплина"])
            WorkLoad.objects.get_or_create(
                teacher=Teacher.objects.get(surname=surname),
                group_name=row["группа"],
                lesson=lesson,
                study=study,
                hours_type=row["вид часов"],
                hours=row["часы"],
                hours_total=row["всего часов (макс)"],
                timing=row["распределение"],
                semester=row["семестр"],
                year=row["год"]
                ) # year = ????
        #Discipline.objects.get(name="nan").delete()
    else:
        form = False
    return render(
        request=request,
        template_name='workWithTables/load.html',
        context={
            'title': 'Загрузка из таблицы *.xls',
            'loaded': form}
    )

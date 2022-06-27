from django.contrib import admin
from .models import *

class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'surname',
        'name', 'second_name', 'birthday_date', 'birthday_place',
        'registration_place', 'cur_place', 'job', 'phone_number',
        'passport', 'TIN', 'INIPA', 'get_academic_degree', 'get_academic_rank',
        'contract', 'fluor_date'
    )
    list_display_links = (
        'id',
        'surname',
        'name',
        'second_name',
        'job'
    )
    search_fields = (
        'id', 'surname', 'birthday_date', 'name', 'second_name', 'job',
        'academic_degree__name', 'academic_rank__name', 'contract__number',
        'contract__end_date'
    )
    def get_academic_degree(self, obj):
        return "\n".join([str(p) for p in obj.academic_degree.all()])
    
    get_academic_degree.short_description = "Ученая степень"

    def get_academic_rank(self, obj):
        return "\n".join([str(p) for p in obj.academic_rank.all()])
    
    get_academic_rank.short_description = "Ученое звание"

class WorkLoadAdmin(admin.ModelAdmin):
    list_display = (
        'teacher', 'group_name', 'lesson', 'study',
        'hours_type', 'hours', 'hours_total', 'timing',
        'semester', 'year'
    )
    list_display_links = (
        'teacher',
    )
    search_fields = (
        'teacher__surname', 'group_name', 'lesson__name', 'study__name',
        'hours_type', 'hours', 'hours_total', 'semester', 'year'
    )

class AcademicDegreeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class AcademicRankAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class DisciplineAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class ContractAdmin(admin.ModelAdmin):
    list_display = (
        'number', 'date', 'end_date', 'wage_rate', 'notes',
    )
    list_display_links = (
        'number',
    )
    search_fields = (
        'number', 'end_date',
    )

# Register your models here.
admin.site.register(AcademicRank, AcademicRankAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(AcademicDegree, AcademicDegreeAdmin)
admin.site.register(WorkLoad, WorkLoadAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Education)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Contract, ContractAdmin)

admin.site.site_title = 'Управление таблицами'
admin.site.site_header = 'Управление таблицами'


from django import forms

W_CHOICE_FIELD = [
    ('teacher', 'фамилия'),
    ('group_name', 'группа'),
    ('lesson', 'занятие'),
    ('study', 'дисциплина'),
    ('hours', 'часы'),
    ('hours_total', 'часы общие'),
    ('year', 'год'),
]

T_CHOICE_FIELD = [
    ('surname', 'фамилия'),
    ('birthday_date', 'дата рождения'),
    ('job', 'должность'),
    ('academic_degree', 'ученая степень'),
    ('academic_rank', 'Ученое звание'),
    ('contract__end_date', 'дата окончания договора'),
]

class WorkLoadSearchForm(forms.Form):
    search_choice = forms.ChoiceField(choices=W_CHOICE_FIELD, label="Искать по ")
    search_input = forms.CharField(max_length=150, label="Ввод ")

class TeacherSearchForm(forms.Form):
    search_choice = forms.ChoiceField(choices=T_CHOICE_FIELD, label="Искать по ")
    search_input = forms.CharField(max_length=150, label="Ввод ")

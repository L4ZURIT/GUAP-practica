from django.urls import path
from .views import TeacherView, export_to_docx, index, loadTable, login, WorkLoadView, TeachersView

urlpatterns = [
    path('', index, name="home"),
    path('login/', login, name="login"),
    path('load/', loadTable, name="load"),
    path('tables/2/', TeachersView.as_view(), name="teachers_table"),
    path('tables/1/', WorkLoadView.as_view(), name="workload_table"),
    path('teacher/<int:pk>/', TeacherView.as_view(), name="teacher_card"),
    path('export/<int:pk>/', export_to_docx, name="export")
]
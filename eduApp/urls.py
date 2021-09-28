from django.urls import path
from .views import (
    SubjectListView,
    TeacherProfileListView,
    TeacherProfileDetailView,
    DayListView,
    GroupListView,
    GroupDetailView,
    StudentListView,
    addStudentToGroup
)

urlpatterns = [
    path('subject-list/', SubjectListView.as_view()),
    path('profile-list/', TeacherProfileListView.as_view()),
    path('profile-list/<int:pk>/', TeacherProfileDetailView.as_view()),
    path('day-list/', DayListView.as_view()),
    path('group-list/', GroupListView.as_view()),
    path('group-list/<int:pk>/', GroupDetailView.as_view()),
    path('student-list/', StudentListView.as_view()),
    path('add-student-to-group/', addStudentToGroup)
]
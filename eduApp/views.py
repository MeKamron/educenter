from django.http import request
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import (
    IsAdminOrReadOnly,
    HasProfile,
    IsOwnerOrReadOnly,
    HasProfileOrNotAllow,
    IsTeacherOrReadOnly
)

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .serializers import (
    SubjectSerializer,
    TeacherProfileSerializer,
    DaySerializer,
    GroupSerializer,
    StudentSerializer
)

from .models import (
    Subject,
    TeacherProfile,
    Day,
    Group,
    Student
)


class SubjectListView(ListCreateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class TeacherProfileListView(ListCreateAPIView):
    serializer_class = TeacherProfileSerializer
    queryset = TeacherProfile.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, HasProfile]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TeacherProfileDetailView(RetrieveUpdateAPIView):
    serializer_class = TeacherProfileSerializer
    queryset = TeacherProfile.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]



class DayListView(ListCreateAPIView):
    serializer_class = DaySerializer
    queryset = Day.objects.all()
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]



class GroupListView(ListCreateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, HasProfileOrNotAllow]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user.profile)


class GroupDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated, IsTeacherOrReadOnly]



class StudentListView(ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(["POST"])
def addStudentToGroup(request):
    if request.method == "POST":
        data = request.data
        for s_id in data["royxat"]:
            student = get_object_or_404(Student, id=s_id)
            student.status = "active"
            student.save()
            guruh = get_object_or_404(Group, id=data["guruh"])
            guruh.students.add(student)
        return Response({"message": "Muvaffaqqiyatli qo'shildi."}, status=200)


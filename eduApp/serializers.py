from rest_framework import serializers
from .models import (
    Subject,
    Day,
    TeacherProfile,
    Group,
    Student
)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name']


class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ["id","date_of_birth", "phone", "address", "subject"]


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    days = DaySerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = ["name", "price", "days", "start", "finish", "students"]





from django.test import TestCase
from .models import Subject, Group, User, TeacherProfile


class SubjectTestCase(TestCase):
    def test_subject_create(self):
        subject = Subject(name="Math")
        self.assertEqual(subject.name, "Math")
    

class GroupTestCase(TestCase):

    def test_group_create(self):
        subject = Subject(name="Math")
        user = User(username="mekamron", password="test_pass")
        teacher = TeacherProfile(
            user=user,
            date_of_birth="2000-08-17",
            phone="+998996051709",
            address="Andijan",
            subject=subject
        )
        group = Group(name="A1", teacher=teacher, start="12:30:00", finish="14:00:00")
        self.assertEqual(group.name, "A1")
        self.assertEqual(group.teacher, teacher)
        self.assertEqual(group.start, "12:30:00")
        self.assertEqual(group.finish, "14:00:00")
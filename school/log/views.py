from log.models import (User, Teacher, Grade, Manager, Program, Student)
from log.logserializers import (
    UserSerializer,
    TeacherSerializer,
    GradeSerializer,
    ManagerSerializer,
    ProgramSerializer,
    StudentSerializer,
    )
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import mixins


class UserModelViewSet(generics.CreateAPIView):
    """api views for users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeacherModelViewSet(viewsets.ModelViewSet):
    """model view set"""
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class GradeViews(viewsets.ModelViewSet):
    """models view for grade"""
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()


class ManagerView(viewsets.ModelViewSet):
    """models view for Managers"""
    serializer_class =ManagerSerializer
    queryset = Manager.objects.all()


class ProgramView(viewsets.ModelViewSet):
    """models for Programme of study"""
    serializer_class=ProgramSerializer
    queryset = Program.objects.all()

class StudentView(viewsets.ModelViewSet):
    """models for students"""
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
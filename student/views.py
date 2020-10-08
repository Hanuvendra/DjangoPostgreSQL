from rest_framework import viewsets
from rest_framework import permissions
from .models import Student
from .serializers import StudentSerializer
from rest_framework.exceptions import PermissionDenied

class IsTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.teacher == request.user

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = (IsTeacher,)
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Student.objects.filter(teacher=user)
        raise PermissionDenied()

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)
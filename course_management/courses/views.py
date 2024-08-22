from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

# Courses Views

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# Course Instances Views

class CourseInstanceCreateView(APIView):
    def post(self, request, *args, **kwargs):
        print("Data: ", request.data)
        serializer = CourseInstanceSerializer(data=request.data)
        print("Serializer Result: ", serializer)
        print("Serializer isValid: ", serializer.is_valid())
        if serializer.is_valid():
            saved = serializer.save()
            print("Saved: ", saved)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseInstanceListView(generics.ListAPIView):
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return CourseInstance.objects.filter(year=year, semester=semester)


class CourseInstanceDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        course_id = self.kwargs['course_id']
        return CourseInstance.objects.get(year=year, semester=semester, course__id=course_id)


# Create your views here.

from django.urls import path
from .views import (
    CourseListCreateView, CourseDetailView,
    CourseInstanceCreateView, CourseInstanceListView, CourseInstanceDetailView
)

urlpatterns = [
    # Course URLs
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),

    # Instance URLs
    path('instances/', CourseInstanceCreateView.as_view(), name='instance-create'),
    path('instances/<int:year>/<int:semester>/', CourseInstanceListView.as_view(), name='instance-list'),
    path('instances/<int:year>/<int:semester>/<int:course_id>/', CourseInstanceDetailView.as_view(), name='instance-detail'),
]

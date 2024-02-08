from django.urls import path
from .views import TeacherDashboardAPIView, TeacherCoursesAPIView, TeacherAssignmentsAPIView, StudentDashboardAPIView, StudentCoursesAPIView, StudentAssignmentSubmissionAPIView, StudentAssignmentsAPIView, test_list, test_detail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('teacher/dashboard/', TeacherDashboardAPIView.as_view(), name='get_teacher_dashboard'),
    path('teacher/courses/', TeacherCoursesAPIView.as_view(), name='teacher_courses'),
    path('teacher/assignments/', TeacherAssignmentsAPIView.as_view(), name='teacher_assignments'),
    path('student/dashboard', StudentDashboardAPIView.as_view(), name='student_dashboard'),
    path('student/courses', StudentCoursesAPIView.as_view(), name='student_courses'),
    path('student/assignments/', StudentAssignmentSubmissionAPIView.as_view(), name='submit_assignment'),
    path('student/assignments/', StudentAssignmentsAPIView.as_view(), name='get_student_assignments'),

    ### testing ###
    path('test_list/', test_list, name='test_list'), 
    path('test_detail/<int:id>', test_detail, name='test_detail'), # no trailing slash so suffixes work
]

urlpatterns = format_suffix_patterns(urlpatterns)
from rest_framework import serializers
from .models import TeacherDashboardData, Notification, TeacherSummaryInfo, Course, Assignment, StudentSummaryInfo, StudentDashboardData
from .models import Test

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'title', 'message']

class TeacherSummaryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSummaryInfo
        fields = ['total_teacher_classes', 'total_teacher_assignments', 'upcoming_teacher_deadlines']

class TeacherDashboardDataSerializer(serializers.ModelSerializer):
    notifications = NotificationSerializer(many=True)
    summary_info = TeacherSummaryInfoSerializer()
    
    class Meta:
        model = TeacherDashboardData
        fields = ['summary_info', 'notifications']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'course', 'text', 'questions', 'mark_schemes', 'is_completed']

class StudentSummaryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSummaryInfo
        fields = ['total_student_classes', 'total_student_assignments', 'upcoming_student_deadlines']

class StudentDashboardDataSerializer(serializers.ModelSerializer):
    summary_info = StudentSummaryInfoSerializer()
    notifications = NotificationSerializer(many=True)

    class Meta:
        model = StudentDashboardData
        fields = ['summary_info', 'notifications']








### testing ###
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'field_a', 'field_b']
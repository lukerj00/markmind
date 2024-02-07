from rest_framework import serializers
from .models import TeacherDashboardData, Notification, TeacherSummaryInfo, Course, Assignment
from .models import Test

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'title', 'message']

class SummaryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSummaryInfo
        fields = ['total_teacher_classes', 'total_teacher_assignments', 'upcoming_teacher_deadlines']

class TeacherDashboardDataSerializer(serializers.ModelSerializer):
    notifications = NotificationSerializer(many=True)
    summary_info = SummaryInfoSerializer()
    
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



### testing ###
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'field_a', 'field_b']
# from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from .models import TeacherDashboardData, Course, Assignment, StudentDashboardData, Test
from .serializers import TeacherDashboardDataSerializer, CourseSerializer, AssignmentSerializer, StudentDashboardDataSerializer, SubmissionSerializer, TestSerializer
from rest_framework.decorators import api_view # fnc-based
from rest_framework.views import APIView # class-based
from rest_framework.response import Response
from rest_framework import status

class TeacherDashboardAPIView(APIView):
    def get(self, request):
        try:
            get_teacher_dashboard = TeacherDashboardData.objects.all() # use .get(teacher=request.user) at some point when users are implemented
            serializer = TeacherDashboardDataSerializer(get_teacher_dashboard, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TeacherDashboardData.DoesNotExist:
            return Response({"message": "dashboard data not found"}, status=status.HTTP_404_NOT_FOUND)

class TeacherCoursesAPIView(APIView):
    def get(self, request):
        try:
            courses = Course.objects.all()
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({"message": "courses not found"}, status=status.HTTP_404_NOT_FOUND)

class TeacherAssignmentsAPIView(APIView):
    def get(self, request):
        queryset = Assignment.objects.all()
        course_id = request.query_params.get('courseId')
        is_completed = request.query_params.get('isCompleted')

        if course_id:
            queryset = queryset.filter(course_id=course_id)
        if is_completed is not None:
            queryset = queryset.filter(is_completed=is_completed.lower() in ['true', '1'])

        serializer = AssignmentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDashboardAPIView(APIView):
    def get(self, request):
        try:
            dashboard_data = StudentDashboardData.objects.all() # # use .get(student=request.user) at some point when users are implemented
            serializer = StudentDashboardDataSerializer(dashboard_data)
            return Response(serializer.data)
        except StudentDashboardData.DoesNotExist:
            return Response({"message": "student dashboard data not found."}, status=status.HTTP_404_NOT_FOUND)

class StudentCoursesAPIView(APIView):
    def get(self, request):
        try:
            courses = Course.objects.all()
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({"message": "courses not found"}, status=status.HTTP_404_NOT_FOUND)
        
class StudentAssignmentSubmissionAPIView(APIView):
    def post(self, request):
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentAssignmentsAPIView(APIView): # new class as different resource
    def get(self, request):
        queryset = Assignment.objects.all()
        course_id = request.query_params.get('courseId')
        # is_due = request.query_params.get('isDue')

        if course_id:
            queryset = queryset.filter(course__id=course_id) # double underscore for foreign key field (course is a foreign key field on the assignment model, and __ performs a join)
        # implement is_due filter at some point
        # if is_due:
        #     try:
        #         is_due_date = datetime.strptime(is_due, '%d/%m/%Y').date()
        #         queryset = queryset.filter(due_date__lte=is_due_date) # less than or equal to due date
        #     except ValueError:
        #         # incorrect date format
        #         return Response({"error": "incorrect date format. should be 'DD/MM/YYYY'."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = AssignmentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def get(self, request):
    #     # implement - fetch student based on request user (customize as needed)
    #     student = Student.objects.filter(user=request.user).first()
    #     if not student:
    #         return Response({"message": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
        
    #     courses = student.courses.all()
    #     if courses:
    #         serializer = CourseSerializer(courses, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(status=status.HTTP_204_NO_CONTENT)
















### testing ###
@api_view(['GET','POST'])
def test_list(request, format=None):

    if request.method == 'GET':
        
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def test_detail(request, id, format=None):

    try:
        test = Test.objects.get(pk=id)
    except Test.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TestSerializer(test)
        return Response(serializer.data)
    elif request.method == 'PUT': # note need to include id in json data for PUT
        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





    # return render(request, 'api/test_list.html', {})

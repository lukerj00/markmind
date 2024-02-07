# from django.shortcuts import render
from django.http import JsonResponse
from .models import TeacherDashboardData, Course, Assignment, Test
from .serializers import TeacherDashboardDataSerializer, CourseSerializer, AssignmentSerializer, TestSerializer
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

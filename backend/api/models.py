from django.db import models

class TeacherSummaryInfo(models.Model):
    total_teacher_classes = models.IntegerField()
    total_teacher_assignments = models.IntegerField()
    upcoming_teacher_deadlines = models.IntegerField()

class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()  # Use TextField for longer text

    def __str__(self):
        return self.title

class TeacherDashboardData(models.Model):
    summary_info = models.OneToOneField(TeacherSummaryInfo, on_delete=models.CASCADE)
    notifications = models.ManyToManyField(Notification)

class StudentSummaryInfo(models.Model):
    total_student_classes = models.IntegerField()
    total_student_assignments = models.IntegerField()
    upcoming_student_deadlines = models.IntegerField()

class StudentDashboardData(models.Model):
    summary_info = models.OneToOneField(StudentSummaryInfo, on_delete=models.CASCADE)
    notifications = models.ManyToManyField(Notification)

class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments') # stored as course_id in db
    text = models.TextField(default='')  # Use TextField for longer text
    questions = models.JSONField()  # store questions as JSON list in a single db column
    mark_schemes = models.JSONField()  # storing mark schemes as JSON list in a single db column
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"assignment {self.id} for course {self.course_id}"
    
class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions') # stored as assignment_id in db
    course = models.ForeignKey(Course, on_delete=models.CASCADE) # stored as course_id in db
    answers = models.JSONField()  # storing answers as JSON list in a single db column

    def __str__(self):
        return f"submission {self.id} for assignment {self.assignment_id}"












### testing ###
class Test(models.Model):
    field_a = models.CharField(max_length=50)
    field_b = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.field_a
    
from django.db import models

class Certificate(models.Model):
    cert_id = models.CharField(max_length=66, primary_key=True)
    student_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student_name} - {self.course_name}'
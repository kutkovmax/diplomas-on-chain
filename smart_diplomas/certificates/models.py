from django.db import models

from django.db import models

class Certificate(models.Model):
    student_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    issued_at = models.DateTimeField(auto_now_add=True)
    blockchain_address = models.CharField(max_length=255)
    certificate_hash = models.CharField(max_length=66)


    def __str__(self):
        return  f'{self.student_name} - {self.course_name}'
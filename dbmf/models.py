from django.db import models




class Course(models.Model):
    title   = models.CharField(max_length=50)
    code    = models.CharField(max_length=10)

    def __str__(self):
        return self.code

class CoursePrereq(models.Model):
    code1   = models.CharField(max_length=10)
    code2   = models.CharField(max_length=10)

    def __str__(self):
        return self.code1

class UserTakenCourse(models.Model):
    user_id     = models.CharField(max_length=10)
    course_code = models.CharField(max_length=10)
    lecturer_id = models.CharField(max_length=10)
    def __str__(self):
        return self.course_code

class Lecturer(models.Model):
    name        = models.CharField(max_length=250)
    vote_count = models.IntegerField(blank=True, null=True)
    vote_avg = models.DecimalField(max_digits=5, decimal_places=0, null = True)
    def __str__(self):
        return self.name

class CRNS(models.Model):
    course_name = models.CharField(max_length=64, null = True)
    course_code = models.CharField(max_length=64, null = True)
    day = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    room = models.CharField(max_length=64, null=True)
    building = models.CharField(max_length=64, null=True)
    lecturer = models.CharField(max_length=64, null=True)
    crn = models.CharField(max_length=64, null=True)
    time_start = models.CharField(max_length=64, null=True)
    time_stop = models.CharField(max_length=64, null=True)
    avgScore = models.DecimalField(max_digits=5, decimal_places=1, null = True)
    capacity = models.DecimalField(max_digits=5, decimal_places=0, null = True)
    enrolled = models.DecimalField(max_digits=5, decimal_places=0, null = True)

    def __str__(self):
        return str(self.crn)

class TempCRNS(models.Model):
    course_name = models.CharField(max_length=64, null = True)
    course_code = models.CharField(max_length=64, null = True)
    day = models.CharField(max_length=64, null=True)
    time = models.CharField(max_length=64, null=True)
    room = models.CharField(max_length=64, null=True)
    building = models.CharField(max_length=64, null=True)
    lecturer = models.CharField(max_length=64, null=True)
    crn = models.CharField(max_length=64, null=True)
    time_start = models.CharField(max_length=64, null=True)
    time_stop = models.CharField(max_length=64, null=True)
    avgScore = models.DecimalField(max_digits=5, decimal_places=1, null = True)
    capacity = models.DecimalField(max_digits=5, decimal_places=0, null = True)
    enrolled = models.DecimalField(max_digits=5, decimal_places=0, null = True)

    def __str__(self):
        return str(self.crn)

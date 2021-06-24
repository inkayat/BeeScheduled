from django.contrib import admin

from .models import Course
from .models import CoursePrereq
from .models import UserTakenCourse
from .models import Lecturer, CRNS

admin.site.register(Course)
admin.site.register(CoursePrereq)
admin.site.register(UserTakenCourse)
admin.site.register(Lecturer)
admin.site.register(CRNS)

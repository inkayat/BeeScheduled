from django.views.generic.base import TemplateView
from django.shortcuts import render
from dbmf.models import Course, CoursePrereq, Lecturer, UserTakenCourse, CRNS, TempCRNS
from django.contrib.auth.decorators import login_required

class Index(TemplateView):
    template_name = 'pages/index.html'


class OpenSourceView(TemplateView):
    template_name = 'pages/open_source.html'


class AboutPage(TemplateView):
	"""docstring for About"""
	template_name = 'pages/about.html'


class SignUpPage(TemplateView):
    template_name = 'pages/signup.html'


class RateLecturer(TemplateView):
    template_name = 'pages/rate_lecturer.html'

    def get(self, request):
        if request.user.id != None:
            lecturer_list = Lecturer.objects.all()
            return render(request, self.template_name, {'lecturers': lecturer_list})
        else:
            return render(request, 'pages/signup.html')
    def post(self, request):
        rates = request.POST.getlist('rates[]')
        i = 0
        for entry in rates:
            if entry != '0':
                lecturers = Lecturer.objects.all()
                lecturer = lecturers[i]
                total = lecturer.vote_count * float(lecturer.vote_avg)
                lecturer.vote_count += 1
                total += float(entry)
                avg = total/lecturer.vote_count
                lecturer.vote_avg = avg
                lecturer.save()
            i+=1

        lecturers = Lecturer.objects.all()
        for item in lecturers:
            print("score: ", item.vote_avg)
        return render(request,'pages/rate_lecturer.html',{'lecturers': lecturers})

class TakenCourseView(TemplateView):
    template_name = 'pages/taken_course.html'

    def get(self, request):
        if request.user.id != None:
            course_list = Course.objects.all()
            return render(request, 'pages/taken_course.html', {'courses': course_list})
        else:
            return render(request, 'pages/signup.html')
    def post(self, request):
        checks = request.POST.getlist('checks[]')

        for entry in checks:
            new = UserTakenCourse(user_id=request.user.id, course_code =entry, lecturer_id = "11")
            new.save()
        return render(request,'pages/open_source.html')


class Profile(TemplateView):
    template_name = 'pages/profile.html'

    def get(self, request):
        if request.user.id != None:
            course_list = UserTakenCourse.objects.all()
            real_list = list()
            for item in course_list:
                if(int(item.user_id) == int(request.user.id)):
                    real_list.append(item.course_code)
            all_courses = Course.objects.all()
            new = list()

            for item in all_courses:
                if(item.code+'/' in real_list):
                    new.append(item)
            return render(request, 'pages/profile.html', {'courses': new})
        else:
            return render(request, 'pages/signup.html')

    def post(self, request):
        delete_crs = request.POST.get('course_to_delete')
        print("delete: ", delete_crs)
        i = 0

        UserTakenCourse.objects.get(course_code=delete_crs+'/').delete()
        if request.user.id != None:
            course_list = UserTakenCourse.objects.all()
            real_list = list()
            for item in course_list:
                if(int(item.user_id) == int(request.user.id)):
                    real_list.append(item.course_code)
            all_courses = Course.objects.all()
            new = list()

            for item in all_courses:
                if(item.code+'/' in real_list):
                    new.append(item)
            return render(request, 'pages/profile.html', {'courses': new})
        else:
            return render(request, 'pages/signup.html')


class GeneratorSchedule(TemplateView):
    template_name = 'pages/schedule_generator.html'

class CreateSchedule(TemplateView):

    template_name  = 'pages/create_schedule.html'
    def get(self,request):
        TempCRNS.objects.all().delete()
        lecturers = Lecturer.objects.all()

        crn_lists=CRNS.objects.all()
        print("list: ", crn_lists)
        print("-----------")
        pre = CoursePrereq.objects.all()
        taken_course = UserTakenCourse.objects.all()
        pre_c1 = list()
        pre_c2 = list()
        user_taken = list()
        for i in pre:
            pre_c1.append(i.code1)
            pre_c2.append(i.code2)
        for i in taken_course:
            print("taken: ", i.course_code)
            print("user_id: ", i.user_id)
            print("curr_user_id: ", request.user.id)

            if int(i.user_id) == int(request.user.id):
                user_taken.append(i.course_code)
                print("yeah, taken: ", i.course_code)


        for x in crn_lists:
            for y in lecturers:
                if x.lecturer == y.name:
                    x.avgScore = y.vote_avg
                    x.save()
        crn_lists=CRNS.objects.all()
        print("list: ", crn_lists)
        for x in crn_lists:
            if x.course_code in pre_c1:
                print("in")
                index = pre_c1.index(x.course_code)
                print("index: ", index)
                print("taken_code: ", x.course_code)
                if pre_c2[index]+'/' in user_taken:
                    print("Yes taken: ", x.course_code)
                    new = TempCRNS(course_name=x.course_name, course_code = x.course_code, day = x.day, time = x.time,room= x.room, building = x.building, lecturer= x.lecturer, crn = x.crn, time_start=x.time_start ,time_stop = x.time_stop, avgScore = x.avgScore, capacity = x.capacity, enrolled = x.enrolled)
                    new.save()
            else:
                new = TempCRNS(course_name=x.course_name, course_code = x.course_code, day = x.day, time = x.time,room= x.room, building = x.building, lecturer= x.lecturer, crn = x.crn, time_start=x.time_start ,time_stop = x.time_stop, avgScore = x.avgScore, capacity = x.capacity, enrolled = x.enrolled)
                new.save()



        crn_lists=TempCRNS.objects.all().order_by('course_name', '-avgScore')

        #crn_lists=CRNS.objects.all().order_by('course_name', '-avgScore')
        #TempCRNS.objects.all().delete()
        return render(request,self.template_name,{'crns':crn_lists})

    def post(self,request):
        checks = request.POST.getlist('checks[]')
        desired_lists = []


        for x in checks:
            desired_lists.append((CRNS.objects.get(crn__contains = x)))

        return render(request,'pages/schedule_generator.html',{'conc':desired_lists})

from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from .models import Time, Course
import json
import time as t

# Create your views here.
def index(request):
    template = 'curriculum/index.html'

    if request.method == 'GET':

        sql = "SELECT name FROM "

        return render(request, template)

    if request.method == 'POST':
        data = dict(request.POST)
        print(data)

        if data['type'][0] == 'empty':
            empty_search = data['empty_search[]']
            ans = set()
            searchset = set()

            # sql = '''SELECT c.name, t.week, t.period
            #          FROM curriculum_course as c,
            #                 curriculum_coursetime as ct,
            #                 curriculum_time as t
            #          WHERE c.id = ct.course_id and ct.time_id = t.id;'''

            sql = '''
                SELECT c.id, c.name, cl.name, t.name, c.time, c.credit
                FROM (curriculum_course as c join curriculum_teacher as t on t.id = teacher_id)
                JOIN curriculum_classes as cl ON cl.id = c.classes_id
            '''

            for i in empty_search:
                i = int(i)
                week = (i % 5) + 1
                period = int(i / 5) + 1

                searchset.add(
                    (week, period)
                )

            with connection.cursor() as c:
                c.execute(sql)
                all_courseid = c.fetchall()

            print(all_courseid)

            c = connection.cursor()

            for i in all_courseid:
                sql = '''
                        SELECT week, period
                        FROM curriculum_coursetime AS ct , 
                               curriculum_time AS t
                        WHERE ct.course_id = "''' + i[0] + '''" 
                        AND ct.time_id = t.id
                    '''

                c.execute(sql)
                temp = c.fetchall()
                com = set(temp)
                if com.issubset(searchset) and com != set():
                    ans.add(i)

            c.close()

            response = JsonResponse({'result': list(ans)})

            return response

    return render(request, template)


# def control(request):
#     template = 'curriculum/control.html'
#
#     if request.method == "GET":
#         return render(request, template)
#
#     filename = request.POST.get('filename')
#     file = request.FILES.get('data')
#
#     print(file)
#
#     return render(request, template)

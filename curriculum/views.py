from django.shortcuts import render
from django.http import JsonResponse
from .models import Time, Course
import json
import time as t

# Create your views here.
def index(request):
    template = 'curriculum/index.html'

    if request.method == 'POST':
        data = dict(request.POST)
        empty_search = data['empty_search[]']
        ans = []
        searchset = set()

        for i in empty_search:
            i = int(i)
            week = (i % 5) + 1
            period = int(i / 5) + 1

            searchset.add(Time.objects.get(week=week, period=period))

        all_course = tuple(Course.objects.all())

        start = t.time()
        for i in all_course:
            temp = tuple(i.coursetime_set.all())
            com = set()

            for j in temp:
                com.add(j.time)
            if com.issubset(searchset) and com != set():
                ans.append(i)
        end = t.time()
        print(end - start)

        # response = JsonResponse({'good': 'GOOD', 'result': ans})

        return render(request, template, {'result': ans})
        # return response

    return render(request, template)

def control(request):
    template = 'curriculum/control.html'

    if request.method == "GET":
        return render(request, template)

    filename = request.POST.get('filename')
    file = request.FILES.get('data')

    print(file)

    return render(request, template)

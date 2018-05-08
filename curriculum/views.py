from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'curriculum/index.html'

    return render(request, template)

def control(request):
    template = 'curriculum/control.html'



    return render(request, template)
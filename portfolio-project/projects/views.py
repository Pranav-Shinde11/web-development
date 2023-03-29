from django.shortcuts import render,get_object_or_404
from .models import project 

# Create your views here.
def pranav(request):
    projects = project.objects
    return render(request, 'projects/home.html',{'projects': projects})

def detail (request,project_id):
    project_detail = get_object_or_404(project, pk=project_id)
    return render (request, 'projects/detail.html', {'project':project_detail})

import git

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from projects.models import Project


# Create your views here.

# project views
def all_projects(request):
    # query DB and return all project objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html',
                  {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)

    return render(request, 'projects/project_detail.html',
                  {'project':project})

@csrf_exempt
def update_server(request):
    if request.method == 'POST':
        repo = git.Repo('https://www.pythonanywhere.com/user/jtatecc27/files/home/jtatecc27/MyPortfolio')
        origin = repo.remotes.origin

        origin.pull()
        return HttpResponse('Python Anywhere Code Updated')
    else:
        return HttpResponse('Code Not Updated')
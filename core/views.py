from django.shortcuts import render

# Create your views here.


def index(request):
    tasks = request.user.task_set.all()
    data = {
        'tasks': tasks,
        'user': request.user,
    }
    return render(request, 'core/index.html', context=data)
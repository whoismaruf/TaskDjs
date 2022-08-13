from django.shortcuts import render

# Create your views here.


def index(request):
    try:
        tasks = request.user.task_set.all()
        user = request.user
    except:
        tasks = []
        user = None
    data = {
        'tasks': tasks,
        'user': user,
    }
    return render(request, 'core/index.html', context=data)
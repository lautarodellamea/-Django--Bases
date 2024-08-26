from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404  # para manejar el error 404

# importo mis formularios
from .forms import CreateNewTask, CreateNewProject


def index(request):

    title = "Django Course!"

    return render(request, 'index.html', {'title': title})


def about(request):

    lista = [1, 2, 3]

    usernameDiccionary = {
        "name": "lautaro"
    }

    username = "lautaro"

    return render(request, 'about.html', {'username': username})
    # return(HttpResponse("<h1>About</h1>"))


# PARAMS
def helloName(request, name):
    print(name)
    return (HttpResponse("<h1>Hello %s</h1>" % name))


def helloId(request, id):

    print(type(id))  # ver tipo de dato del id, podria hacer conversiones si quisiera
    result = id * 2

    return (HttpResponse("<h1>Hello %s</h1>" % result))


# PARAMS + MODELS
def projects(request):

    # para poder convertirlo a json debo convertirlo en una lista de python primero
    projects = list(Project.objects.values())

    projects = Project.objects.all()

    # return JsonResponse(projects, safe=False)
    return render(request, 'projects/projects.html', {'projects': projects})


def tasksId(request, id):

    # task = Task.objects.get(id=id)
    # si buscamos asi y no existe devuelve 404, y no me tumba el proyecto
    task = get_object_or_404(Task, id=id)

    # return HttpResponse("task: %s" % task.title)
    return render(request, 'tasks/tasks.html', {'task': task})


def tasks(request):

    tasks = Task.objects.all()

    return render(request, 'tasks/tasks.html', {'tasks': tasks})

# CREACION DE TAREAS


def create_task(request):

    # print(request.GET) # vemos lo que escribimos en el form al mandarlo por GET
    # print(request.GET["title"])
    # print(request.GET["description"])

    if request.method == "GET":
        # si me visitan a traves del metodo get, muestro la interfaz
        # show interface - renderizo la interfaz
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })

    else:
        # si me visitan a traves del metodo post, guardo la tarea
        # creamos una tarea con los datos que vienen en el form
        Task.objects.create(
            title=request.POST["title"], description=request.POST["description"], project_id=1)

        # redirecciono, desde la ruta inicial (por eso pongo la primera barra), a la ruta tasks
        # return redirect("/tasks/")
        # paso la ruta con el nombre que le di
        return redirect("tasks")


# CREACION DE PROJECT
def create_project(request):

    if request.method == "GET":
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })

    else:

        # print(request.POST)

        project = Project.objects.create(name=request.POST["name"])
        # print(project)

        return redirect("projects")


def project_detail(request, id):

    print(id)
    # project = Project.objects.get(id=id)
    # get_object_or_404 si buscamos un objeto y no lo encuentra devuelve 404
    # get_object_or_404 si buscamos una lista y no lo encuentra devuelve 404
    project = get_object_or_404(Project, id=id)

    # obtenemos la tarea del proyecto correspondiente
    tasks = Task.objects.filter(project_id=id)

    # print(project)

    return render(request, 'projects/project_detail.html', {
        'project': project,
        'tasks': tasks

    })

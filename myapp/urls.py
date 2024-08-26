
from django.urls import path
from . import views

urlpatterns = [

    # path('', views.index),
    # de esta forma puedo nombrar rutas, y en caso de cambiar su nombre impacta en todos lados
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    # params
    # http://127.0.0.1:3000/myapp/hello/lautaro
    # debo definir el segundo parametro en la funcion  "hello", para que esta lo pueda leer
    path('hello/<str:name>', views.helloName, name='helloName'),
    path('hello2/<int:id>', views.helloId, name='helloId'),

    # Params + Models
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:id>', views.tasksId, name='tasksId'),

    # creacion de tareas
    path('create_task/', views.create_task, name='create_task'),

    # creacion de proyectos
    path('create_project/', views.create_project, name='create_project'),

    path('project/<int:id>', views.project_detail, name='project_detail'),

]

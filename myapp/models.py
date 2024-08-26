from django.db import models

class Project(models.Model): # Definimos la clase Project, la cual hereda de models.Model de Django
  name=models.CharField(max_length=255)

  # Método especial que devuelve una representación legible del objeto en el panel de administración
  def __str__(self):
    return self.name 



class Task(models.Model):
  title=models.CharField(max_length=255)
  description=models.TextField()
  # description=models.TextField(blank=True, null=True)
  # description=models.TextField(blank=True, null=True, default="")
  # relacion, y al eliminar un dato, en cascada se eliminaran el resto que se relacionen con el
  project=models.ForeignKey(Project, on_delete=models.CASCADE)

  done=models.BooleanField(default=False)

  def __str__(self):
    return self.title + " - " + self.project.name
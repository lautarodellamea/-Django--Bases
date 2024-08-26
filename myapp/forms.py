from django import forms

""" a traves de este archivo django construye el formulario """


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea",
                            max_length=200,
                            widget=forms.TextInput(attrs={'class': 'mi-input'})
                            )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'mi-input'}),
        label="Descripción de la tarea",
        max_length=500,
    )


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200)

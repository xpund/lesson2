import datetime

from .models import Task
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
import datetime

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "pub_date"]
        now = datetime.datetime.now()
        widgets = {
            "title": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Заголовок задачи',
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите подробный текст задачи',
                'id': 'exampleFormControlTextarea1',
                'rows': 3,
            }),
        }
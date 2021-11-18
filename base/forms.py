from django import forms
from .models import Project, Task

from django.forms import ModelForm

class DateInput(forms.DateInput):
	input_type = 'date'

class ProjectModelForm(ModelForm):
	class Meta:
		model = Project
		fields = ['project_title', 'project_status', 'project_intro', 'project_description', 'project_price', 'project_due_date', 'project_complete']
		widgets = {
			'project_due_date': DateInput()
		}

class TaskModelForm(ModelForm):
	class Meta:
		model = Task
		fields = ['task_title', 'task_belongs', 'task_description', 'task_due_date', 'task_important', 'task_complete']
		widgets = {
			'task_due_date': DateInput()
		}
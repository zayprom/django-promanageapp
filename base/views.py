from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.db.models import Count

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from django import forms
from .forms import ProjectModelForm, TaskModelForm

from django.utils import timezone

from datetime import date

from django.forms import DateInput, ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from .models import Profile, Project, Task

# Create your views here.

class CustomLoginView(LoginView):
	template_name = 'base/login.html'
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('projects')

class RegisterPage(FormView):
	template_name = 'base/register.html'
	form_class = UserCreationForm
	redirect_authenticated_user = True
	success_url = reverse_lazy('projects')

	def form_valid(self, form):
		user = form.save()
		if user is not None:
			login(self.request, user)
		return super(RegisterPage, self).form_valid(form)

	def get(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('projects')
		return super(RegisterPage, self).get(*args, **kwargs)


class ProfileDetail(LoginRequiredMixin, DetailView):
	model = Profile
	context_object_name = 'profile'
	template_name = 'base/profile.html'
	queryset = Profile.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['count_projects'] = Project.objects.filter(owner=self.request.user.profile, project_complete=False).count()
		context ['count_projects_pending'] = Project.objects.filter(owner=self.request.user.profile, project_status='1').count()
		context ['count_projects_active'] = Project.objects.filter(owner=self.request.user.profile, project_status='2').count()
		context ['count_projects_waiting'] = Project.objects.filter(owner=self.request.user.profile, project_status='3').count()
		context ['count_projects_finished'] = Project.objects.filter(owner=self.request.user.profile, project_status='4').count()
		context ['count_tasks'] = Task.objects.filter(owner=self.request.user.profile, task_complete=False).count()

		return context


class ProfileUpdate(LoginRequiredMixin, UpdateView):
	model = Profile
	fields = ['username', 'email']
	success_url = reverse_lazy('projects')
	queryset = Profile.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['count_projects'] = Project.objects.filter(owner=self.request.user.profile, project_complete=False).count()
		context ['count_projects_pending'] = Project.objects.filter(owner=self.request.user.profile, project_status='1').count()
		context ['count_projects_active'] = Project.objects.filter(owner=self.request.user.profile, project_status='2').count()
		context ['count_projects_waiting'] = Project.objects.filter(owner=self.request.user.profile, project_status='3').count()
		context ['count_projects_finished'] = Project.objects.filter(owner=self.request.user.profile, project_status='4').count()
		context ['count_tasks'] = Task.objects.filter(owner=self.request.user.profile, task_complete=False).count()

		return context

class ProjectList(LoginRequiredMixin, ListView):
	model = Project
	context_object_name = 'projects'
	queryset = Project.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['projects'] = context ['projects'].filter(owner = self.request.user.profile)
		context ['count_projects'] = context ['projects'].filter(project_complete=False).count()
		context ['count_projects_pending'] = Project.objects.filter(owner=self.request.user.profile, project_status='1').count()
		context ['count_projects_active'] = Project.objects.filter(owner=self.request.user.profile, project_status='2').count()
		context ['count_projects_waiting'] = Project.objects.filter(owner=self.request.user.profile, project_status='3').count()
		context ['count_projects_finished'] = Project.objects.filter(owner=self.request.user.profile, project_status='4').count()
		context ['count_tasks'] = Task.objects.filter(owner=self.request.user.profile, task_complete=False).count()

		search_input = self.request.GET.get('search-area') or ''
		if search_input:
			context['projects'] = context['projects'].filter(project_title__icontains=search_input)

		context['search_input'] = search_input
		return context


class ProjectDetail(LoginRequiredMixin, DetailView):
	model = Project
	context_object_name = 'project'
	template_name = 'base/project.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['count_projects'] = Project.objects.filter(owner=self.request.user.profile, project_complete=False).count()
		context ['count_projects_pending'] = Project.objects.filter(owner=self.request.user.profile, project_status='1').count()
		context ['count_projects_active'] = Project.objects.filter(owner=self.request.user.profile, project_status='2').count()
		context ['count_projects_waiting'] = Project.objects.filter(owner=self.request.user.profile, project_status='3').count()
		context ['count_projects_finished'] = Project.objects.filter(owner=self.request.user.profile, project_status='4').count()
		context ['count_tasks'] = Task.objects.filter(owner=self.request.user.profile, task_complete=False).count()

		return context

class ProjectCreate(LoginRequiredMixin, CreateView):
	model = Project
	form_class = ProjectModelForm
	context_object_name = 'projects'
	queryset = Project.objects.all()
	success_url = reverse_lazy('projects')

	def form_valid(self, form):
		form.instance.owner = self.request.user.profile
		return super(ProjectCreate, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['count_projects'] = Project.objects.filter(owner=self.request.user.profile, project_complete=False).count()
		context ['count_projects_pending'] = Project.objects.filter(owner=self.request.user.profile, project_status='1').count()
		context ['count_projects_active'] = Project.objects.filter(owner=self.request.user.profile, project_status='2').count()
		context ['count_projects_waiting'] = Project.objects.filter(owner=self.request.user.profile, project_status='3').count()
		context ['count_projects_finished'] = Project.objects.filter(owner=self.request.user.profile, project_status='4').count()
		context ['count_tasks'] = Task.objects.filter(owner=self.request.user.profile, task_complete=False).count()

		return context

class ProjectUpdate(LoginRequiredMixin, UpdateView):
	model = Project
	form_class = ProjectModelForm
	success_url = reverse_lazy('projects')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['count_projects'] = Project.objects.filter(owner=self.request.user.profile, project_complete=False).count()
		context ['count_projects_pending'] = Project.objects.filter(owner=self.request.user.profile, project_status='1').count()
		context ['count_projects_active'] = Project.objects.filter(owner=self.request.user.profile, project_status='2').count()
		context ['count_projects_waiting'] = Project.objects.filter(owner=self.request.user.profile, project_status='3').count()
		context ['count_projects_finished'] = Project.objects.filter(owner=self.request.user.profile, project_status='4').count()
		context ['count_tasks'] = Task.objects.filter(owner=self.request.user.profile, task_complete=False).count()

		return context

class DeleteView(LoginRequiredMixin, DeleteView):
	model = Project
	context_object_name = 'project'
	success_url = reverse_lazy('projects')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['count_projects'] = Project.objects.filter(owner=self.request.user.profile, project_complete=False).count()
		context ['count_projects_pending'] = Project.objects.filter(owner=self.request.user.profile, project_status='1').count()
		context ['count_projects_active'] = Project.objects.filter(owner=self.request.user.profile, project_status='2').count()
		context ['count_projects_waiting'] = Project.objects.filter(owner=self.request.user.profile, project_status='3').count()
		context ['count_projects_finished'] = Project.objects.filter(owner=self.request.user.profile, project_status='4').count()
		context ['count_tasks'] = Task.objects.filter(owner=self.request.user.profile, task_complete=False).count()

		return context


class TaskList(LoginRequiredMixin, ListView):
	model = Task
	context_object_name = 'tasks'
	queryset = Task.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['tasks'] = context ['tasks'].filter(owner = self.request.user.profile)
		context ['count_tasks'] = context ['tasks'].filter(task_complete=False).count()
		context ['count_projects'] = Project.objects.filter(owner=self.request.user.profile, project_complete=False).count()
		context ['count_projects_pending'] = Project.objects.filter(owner=self.request.user.profile, project_status='1').count()
		context ['count_projects_active'] = Project.objects.filter(owner=self.request.user.profile, project_status='2').count()
		context ['count_projects_waiting'] = Project.objects.filter(owner=self.request.user.profile, project_status='3').count()
		context ['count_projects_finished'] = Project.objects.filter(owner=self.request.user.profile, project_status='4').count()

		return context


class TaskDetail(LoginRequiredMixin, DetailView):
	model = Task
	context_object_name = 'task'
	template_name = 'base/task.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['count_projects'] = Project.objects.filter(owner=self.request.user.profile, project_complete=False).count()
		context ['count_projects_pending'] = Project.objects.filter(owner=self.request.user.profile, project_status='1').count()
		context ['count_projects_active'] = Project.objects.filter(owner=self.request.user.profile, project_status='2').count()
		context ['count_projects_waiting'] = Project.objects.filter(owner=self.request.user.profile, project_status='3').count()
		context ['count_projects_finished'] = Project.objects.filter(owner=self.request.user.profile, project_status='4').count()
		context ['count_tasks'] = Task.objects.filter(owner=self.request.user.profile, task_complete=False).count()

		return context


class TaskCreate(LoginRequiredMixin, CreateView):
	model = Task
	form_class = TaskModelForm
	context_object_name = 'tasks'
	queryset = Task.objects.all()
	success_url = reverse_lazy('tasks')

	def get_form(self, *args, **kwargs):
		form = super(TaskCreate, self).get_form(*args, **kwargs)
		form.fields['task_belongs'].queryset = Project.objects.filter(owner=self.request.user.profile)
		return form


	def form_valid(self, form):
		form.instance.owner = self.request.user.profile
		return super(TaskCreate, self).form_valid(form)


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['count_projects'] = Project.objects.filter(owner=self.request.user.profile, project_complete=False).count()
		context ['count_projects_pending'] = Project.objects.filter(owner=self.request.user.profile, project_status='1').count()
		context ['count_projects_active'] = Project.objects.filter(owner=self.request.user.profile, project_status='2').count()
		context ['count_projects_waiting'] = Project.objects.filter(owner=self.request.user.profile, project_status='3').count()
		context ['count_projects_finished'] = Project.objects.filter(owner=self.request.user.profile, project_status='4').count()
		context ['count_tasks'] = Task.objects.filter(owner=self.request.user.profile, task_complete=False).count()

		return context


class TaskUpdate(LoginRequiredMixin, UpdateView):
	model = Task
	form_class = TaskModelForm
	success_url = reverse_lazy('tasks')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context ['count_projects'] = Project.objects.filter(owner=self.request.user.profile, project_complete=False).count()
		context ['count_projects_pending'] = Project.objects.filter(owner=self.request.user.profile, project_status='1').count()
		context ['count_projects_active'] = Project.objects.filter(owner=self.request.user.profile, project_status='2').count()
		context ['count_projects_waiting'] = Project.objects.filter(owner=self.request.user.profile, project_status='3').count()
		context ['count_projects_finished'] = Project.objects.filter(owner=self.request.user.profile, project_status='4').count()
		context ['count_tasks'] = Task.objects.filter(owner=self.request.user.profile, task_complete=False).count()

		return context



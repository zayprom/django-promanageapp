from django.urls import path
from .views import ProjectList, ProjectDetail, ProjectCreate, ProjectUpdate, DeleteView, TaskList, TaskDetail, TaskCreate, TaskUpdate, ProfileDetail, ProfileUpdate, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
	path('', ProjectList.as_view(), name='projects'),
	path('project/<int:pk>/', ProjectDetail.as_view(), name='project'),
	path('create-project/', ProjectCreate.as_view(), name='project-create'),
	path('project-update/<int:pk>/', ProjectUpdate.as_view(), name='project-update'),
	path('project-delete/<int:pk>/', DeleteView.as_view(), name='project-delete'),

	path('task-list/', TaskList.as_view(), name='tasks'),
	path('create-task/', TaskCreate.as_view(), name='task-create'),
	path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),

	path('profile/<int:pk>/', ProfileDetail.as_view(), name = 'profile'),
	path('profile-update/<int:pk>/', ProfileUpdate.as_view(), name = 'profile-update'),

	path('login/', CustomLoginView.as_view(), name = 'login'),
	path('logout/', LogoutView.as_view(next_page='login'), name = 'logout'),
	path('register/', RegisterPage.as_view(), name = 'register'),
]
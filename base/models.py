from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import date

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	email = models.EmailField(max_length = 500, null=True, blank=True)
	username = models.CharField(max_length = 200, blank = True, null = True)

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

	def __str__(self):
		return str(self.user.username)

class Project(models.Model):
	CHOICES = [
		('1', 'Pending'),
		('2', 'Active'),
		('3', 'Waiting'),
		('4', 'Invoiced')
		]
	

	owner = models.ForeignKey(Profile, on_delete = models.CASCADE, null = True, blank = True)
	project_title = models.CharField(max_length=200,null=True, blank=True)
	project_intro = models.CharField(max_length=300,null=True, blank=True)
	project_description = models.TextField(blank=True, null=True)
	project_status = models.CharField(choices = CHOICES, max_length=200, null=True, blank=True)
	project_price = models.CharField(max_length=100,null=True, blank=True)
	project_complete = models.BooleanField(default=False)
	project_create = models.DateTimeField(auto_now_add=True)
	project_due_date = models.DateField(auto_now_add=False, null=True, blank=False)

	def is_due_date(self):
		return date.today() < self.project_due_date

	def __str__(self):
		return str(self.project_title)

	class Meta:
		ordering = ['project_complete']

class Task(models.Model):
	owner = models.ForeignKey(Profile, on_delete = models.CASCADE, null = True, blank = True)
	task_title = models.CharField(max_length=200,null=True, blank=True)
	task_belongs = models.ForeignKey(Project, on_delete = models.CASCADE, null = True, blank = True)
	task_description = models.CharField(max_length=300, null=True, blank=True)
	task_due_date = models.DateField(auto_now_add=False,null=True, blank=False)
	task_important = models.BooleanField(default=False)
	task_complete = models.BooleanField(default=False)
	task_create = models.DateTimeField(auto_now_add=True)

	#vždy uvést datum u tasku
	def is_task_due_date(self):
		return date.today() < self.task_due_date

	def __str__(self):
		return str(self.task_title)
		
	class Meta:
		ordering = ['task_complete']



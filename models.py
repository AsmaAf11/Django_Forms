from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, help_text='project name')
    creation_time = models.DateTimeField(auto_now_add=True, help_text='creation time')
    completion_time = models.DateTimeField(null=True, help_text='completion time')
    image_field = models.ImageField(upload_to="images/")
    project_logo= models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name
               #+ '' + str(self.creation_time) + '' + str(self.completion_time)


class Task(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text='Task name')
    description = models.TextField(help_text='Task name')
    time_estimate = models.IntegerField(help_text='creation time')
    completed = models.BooleanField(default=False)


#Task = Task.object.create(Project="MyProject", title="First task", description="the task's info ", time_estimate='4', completed=True)

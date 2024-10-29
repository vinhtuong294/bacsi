from django.db import models
# Create your models here.
class Project(models.Model):
    P_name = models.CharField(
        max_length=70,
        help_text="The name of the project.")
    starting_date = models.DateField(
        verbose_name="Date the project was started.")
    P_ID = models.CharField(
        max_length=20,
        verbose_name="ID number of the project.")

    def __str__(self):
        return self.P_name


class Task(models.Model):
    T_name = models.CharField(
        max_length=50,
        help_text="The name of the task.")
    starting = models.DateField(
        verbose_name="Date the task was started.")
    email = models.EmailField(help_text="The contact email for the representative.")
    Project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE, related_name='task_set')

    def __str__(self):
        return self.T_name


class ProjectTask(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_task_set')
    Task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE)


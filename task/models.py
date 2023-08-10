from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(to=TaskType, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("1", "High Priority"),
        ("2", "Medium Priority"),
        ("3", "Low Priority")
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField()
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default="3"
    )
    task_type = models.ForeignKey(to=TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(to=Worker, related_name="tasks")

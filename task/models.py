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

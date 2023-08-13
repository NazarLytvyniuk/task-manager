from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

from task.models import Task


def index(request):
    """View function for the home page of the site."""

    context = {
        "workers": get_user_model().objects.count(),
        "tasks": Task.objects.count()
    }

    return render(request, "task/index.html", context=context)

from django.shortcuts import render
from .models import Announcement


def home(request):
    announcements = Announcement.objects.order_by("-created_at")
    return render(
        request,
        "home.html",
        {
            "message": "Django and PostgreSQL are connected.",
            "announcements": announcements,
        },
    )

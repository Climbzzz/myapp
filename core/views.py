from django.shortcuts import render
from .models import Announcement


def home(request):
    announcements = Announcement.objects.select_related("category").order_by(
        "-created_at"
    )
    return render(
        request,
        "home.html",
        {
            "message": "Announcements and their categories",
            "announcements": announcements,
        },
    )

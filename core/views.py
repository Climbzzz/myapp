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

from django.db.models import ProtectedError
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import AnnouncementForm
from .models import Announcement


class AnnouncementListView(ListView):
    model = Announcement
    template_name = "announcements/list.html"
    context_object_name = "announcements"

    def get_queryset(self):
        return Announcement.objects.select_related("category").order_by(
            "-created_at", "-pk"
        )


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = "announcements/detail.html"
    context_object_name = "announcement"

    def get_queryset(self):
        return Announcement.objects.select_related("category")


class AnnouncementCreateView(CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = "announcements/form.html"
    success_url = reverse_lazy("announcement-list")


class AnnouncementUpdateView(UpdateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = "announcements/form.html"
    success_url = reverse_lazy("announcement-list")


class AnnouncementDeleteView(DeleteView):
    model = Announcement
    template_name = "announcements/confirm_delete.html"
    success_url = reverse_lazy("announcement-list")

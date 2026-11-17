from django.urls import path
from .views import (
    AnnouncementCreateView,
    AnnouncementDeleteView,
    AnnouncementDetailView,
    AnnouncementListView,
    AnnouncementUpdateView,
)

urlpatterns = [
    path("", AnnouncementListView.as_view(), name="announcement-list"),
    path("new/", AnnouncementCreateView.as_view(), name="announcement-create"),
    path("<int:pk>/", AnnouncementDetailView.as_view(), name="announcement-detail"),
    path("<int:pk>/edit/", AnnouncementUpdateView.as_view(), name="announcement-update"),
    path("<int:pk>/delete/", AnnouncementDeleteView.as_view(), name="announcement-delete"),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("announcements/", include("core.urls")),
]

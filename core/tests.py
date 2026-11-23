# Create your tests here.
from django.test import TestCase
from django.urls import reverse

from .models import Announcement, Category


class AnnouncementCrudTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="Workshop Tests")
        cls.announcement = Announcement.objects.create(
            category=cls.category,
            title="Original announcement",
            message="Original announcement message",
        )

    def test_list_displays_announcement(self):
        response = self.client.get(reverse("announcement-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Original announcement")

    def test_create_valid_announcement(self):
        response = self.client.post(
            reverse("announcement-create"),
            {
                "category": self.category.pk,
                "title": "New announcement",
                "message": "A valid new message for testing",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Announcement.objects.filter(title="New announcement").exists()
        )

    def test_create_rejects_short_title(self):
        response = self.client.post(
            reverse("announcement-create"),
            {
                "category": self.category.pk,
                "title": "Hi",
                "message": "A valid message for testing",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "at least 5 characters")
        self.assertFalse(Announcement.objects.filter(title="Hi").exists())

    def test_update_announcement(self):
        response = self.client.post(
            reverse("announcement-update", args=[self.announcement.pk]),
            {
                "category": self.category.pk,
                "title": "Updated announcement",
                "message": "Updated announcement message",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.announcement.refresh_from_db()
        self.assertEqual(self.announcement.title, "Updated announcement")

    def test_get_delete_page_does_not_delete(self):
        response = self.client.get(
            reverse("announcement-delete", args=[self.announcement.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Announcement.objects.filter(pk=self.announcement.pk).exists()
        )

    def test_post_delete_removes_announcement(self):
        response = self.client.post(
            reverse("announcement-delete", args=[self.announcement.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Announcement.objects.filter(pk=self.announcement.pk).exists()
        )

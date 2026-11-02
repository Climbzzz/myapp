#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

from core.models import Announcement

samples = [
    ("WS04: Docker basics", "Docker runs our development services."),
    ("WS04: SQL SELECT", "SELECT retrieves records."),
    ("WS04: SQL WHERE", "WHERE filters records."),
    ("WS04: Django ORM", "The ORM builds SQL from Python."),
    ("WS04: PostgreSQL", "PostgreSQL stores application data."),
]

# Safe to repeat: match on the unique workshop title and update the message.
for title, message in samples:
    Announcement.objects.update_or_create(
        title=title,
        defaults={"message": message},
    )

print("WS04 records:", Announcement.objects.filter(title__startswith="WS04:").count())

from django.shortcuts import render


def home(request):
    return render(
        request,
        "home.html",
        {
            "message": (
                "Hello from a Dockerized Django "
                "application with PostgreSQL!"
            )
        },
    )

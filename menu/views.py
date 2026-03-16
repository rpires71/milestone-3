from django.shortcuts import render


def menu(request):
    """Display the static menu page."""
    return render(request, 'menu.html')
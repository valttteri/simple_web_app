from django.shortcuts import render

# Create your views here.

def indexView(request):
    """Render the front page of the application"""

    contacts = ["mikko", "pekka"]

    return render(
        request,
        "index.html",
        {"contacts": contacts}
    )
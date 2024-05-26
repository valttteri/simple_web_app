from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.

def indexView(request):
    """Render the front page of the application"""

    contacts = Contact.objects.all()

    return render(
        request,
        "index.html",
        {"contacts": contacts}
    )

def addContactView(request):
    """Create a new blog"""

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        number = request.POST.get("number", "").strip()
    
        Contact.objects.create(
            name=name,
            number=number
        )

    return redirect("/")

def removeContactsView(request):
    """Create a new blog"""

    if request.method == "POST":

        Contact.objects.all().delete()

    return redirect("/")
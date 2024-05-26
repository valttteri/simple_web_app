from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Contact

# Create your views here.

@csrf_protect
def indexView(request):
    """Render the front page of the application"""

    contacts = Contact.objects.all()

    return render(
        request,
        "index.html",
        {"contacts": contacts}
    )

@csrf_protect
def addContactView(request):
    """Create a new blog"""

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        number = request.POST.get("number", "").strip()
    
        Contact.objects.create(
            name=name,
            number=number
        )
    
    contacts = Contact.objects.all()

    return render(request, "index.html", {"contacts": contacts})

@csrf_protect
def removeContactsView(request):
    """Create a new blog"""

    if request.method == "POST":

        Contact.objects.all().delete()

    return redirect("/")
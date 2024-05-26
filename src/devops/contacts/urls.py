from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='frontpage'), # the frontpage
    path('addcontact', views.addContactView, name='addcontact'), # add a new contact
    path('removecontacts', views.removeContactsView, name='removecontacts'), # delete all contacts
]
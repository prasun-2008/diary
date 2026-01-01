from .views import dashboard, create_entry, entry_detail, edit_entry, delete_entry
from django.urls import path

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("create/", create_entry, name="create_entry"),
    path("entry/<int:entry_id>/", entry_detail, name="entry_detail"),
    path("entry/<int:entry_id>/edit/", edit_entry, name="edit_entry"),
    path("entry/<int:entry_id>/delete/", delete_entry, name="delete_entry"),
]
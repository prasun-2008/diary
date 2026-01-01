from django.shortcuts import render, redirect, get_object_or_404
from .models import DiaryEntry
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard(request):
    entries = DiaryEntry.objects.filter(owner=request.user)
    return render(request, "diary/dashboard.html", {"entries": entries})

@login_required
def entry_detail(request, entry_id):
    # Get the entry for the logged-in user
    entry = get_object_or_404(DiaryEntry, id=entry_id, owner=request.user)
    return render(request, "diary/entry_detail.html", {"entry": entry})

@login_required
def create_entry(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        DiaryEntry.objects.create(
            title = title,
            content = content,
            owner = request.user
        )
        return redirect("dashboard")

    return render(request,"diary/create_entry.html")


@login_required
def edit_entry(request, entry_id):
    # Get the entry only if it belongs to the logged-in user
    entry = get_object_or_404(DiaryEntry, id=entry_id, owner=request.user)

    if request.method == "POST":
        entry.title = request.POST["title"]
        entry.content = request.POST["content"]
        entry.save()
        return redirect("entry_detail", entry_id=entry.id)

    return render(request, "diary/edit_entry.html", {"entry": entry})

@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id, owner=request.user)

    if request.method == "POST":
        entry.delete()
        return redirect("dashboard")

    return render(request, "diary/delete_entry.html", {"entry": entry})

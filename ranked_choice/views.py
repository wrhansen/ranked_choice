from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET

from .models import Vote


@require_GET
def index(request):
    votes = Vote.objects.all().order_by("-modified")
    return render(request, "index.html", {"votes": votes})


@require_GET
def details(request, pk):
    vote = get_object_or_404(Vote, pk=pk)
    return render(request, "details.html", {"vote": vote})

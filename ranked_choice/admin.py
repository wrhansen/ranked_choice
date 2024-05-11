from django.contrib import admin

from .models import Candidate, Vote


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created", "modified")


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("name", "image")

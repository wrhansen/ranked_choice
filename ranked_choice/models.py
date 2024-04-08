from django.db import models
from django.utils.translation import gettext_lazy as _


class Vote(models.Model):

    class Status(models.TextChoices):
        CREATED = "CR", _("Created")
        OPEN = "OP", _("Open")
        TALLYING = "TL", _("Tallying")
        CLOSED = "CL", _("Closed")

    class Meta:
        indexes = [models.Index(fields=["modified"])]

    name = models.CharField(max_length=128)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.CREATED
    )
    results = models.JSONField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_css_status_class(self):
        statuses = {
            self.Status.CREATED: "text-bg-success",
            self.Status.OPEN: "text-bg-info",
            self.Status.TALLYING: "text-bg-warning",
            self.Status.CLOSED: "text-bg-danger",
        }
        return statuses[self.status]

    def status_label(self):
        return Vote.Status(self.status).label


class Candidate(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()


class UserVote(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    user_candidates = models.JSONField()

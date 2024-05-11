from django.db import models
from django.utils.translation import gettext_lazy as _


class Vote(models.Model):
    """
    A ranked choice voting session
    """

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
    results = models.JSONField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    vote_candidates = models.ManyToManyField("Candidate")

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
    """
    The thing to rank in a vote
    """

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="candidates")

    def __str__(self):
        return f"<Candidate name={self.name} image={self.image.path}>"


class UserVote(models.Model):
    """
    The votes, unique per IP Address
    """

    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name="user_votes")
    ip_address = models.CharField(max_length=128)
    user_candidates = models.JSONField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["ip_address", "vote"]),
        ]

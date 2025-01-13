from django.db import models
from optio.tasks.models import Task


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField()
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="comment",
        blank=False,
        null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Use it to give custom table name and other features available by Django
        """
        pass

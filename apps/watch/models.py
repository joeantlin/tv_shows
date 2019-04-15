from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release = models.DateField()
    desc = models.TextField(default="No description created :(")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Show: {self.title}"

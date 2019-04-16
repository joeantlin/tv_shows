from __future__ import unicode_literals
from django.db import models

class ShowManager(models.Manager):
    def edit_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if 1 <= len(postData['date']) < 10:
            errors["description"] = "Show description should be at least 10 characters"
        return errors
    def add_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if len(postData['date']) < 10:
            errors["date"] = "Invalid Date"
        if 1 <= len(postData["description"]) < 10:
            errors["description"] = "Show description should be at least 10 characters"
        return errors
    
    

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release = models.DateField()
    desc = models.TextField(default="No description created :(")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"Show: {self.title}"


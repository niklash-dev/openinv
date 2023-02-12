from django.db import models

# Create your models here.

class storage_location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class storage_container(models.Model):
    type = models.CharField(max_length=20)
    location = models.ForeignKey(storage_location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.location} {self.type}"

class storage_item(models.Model):
    name = models.CharField(max_length=30)
    container = models.ForeignKey(storage_container, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

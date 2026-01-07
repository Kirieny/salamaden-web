from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

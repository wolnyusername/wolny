from django.db import models


class Worker(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=100)


class Shift(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

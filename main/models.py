from django.db import models


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    comment = models.TextField()
    company = models.OneToOneField(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

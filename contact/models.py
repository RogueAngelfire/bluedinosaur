from django.db import models


class ContactMessages(models.Model):
  name = models.CharField(max_length=254)
  email = models.EmailField(max_length=254, null=False, blank=False)
  projectsummary = models.TextField()

  def __str__(self):
    return self.name

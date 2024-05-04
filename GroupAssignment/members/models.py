from django.db import models
from django.urls import reverse
from catalog.models import Language
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    language_preference = models.ManyToManyField(Language, help_text="Select the preferred languages for books")
    
    def __str__(self) -> str:
        return self.username
    
    def get_absolute_url(self):
        return reverse("member-detail", args=[str(self.id)])
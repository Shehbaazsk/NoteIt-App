from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Note(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    note_title=models.CharField(max_length=255)
    note_body=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.note_title
from django.db import models
from django.contrib.auth.models import User,AbstractUser


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description

class WarningMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    
    

class Banadmin(models.Model):
    is_banned = models.BooleanField(default=False)
    


class Ban(models.Model):
    user1 = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user1_bans')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user2_bans')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.user1.username} ->  حظر  -> {self.user2.username}"

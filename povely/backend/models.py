from django.db import models

# Create your models here.
class User(models.Model):
    # Primary Info
    name=models.CharField(max_length=100)
    nickname=models.CharField(max_length=100, blank=True)
    # dob=models.DateTimeField(auto_now_add=False, blank=True)
    email=models.EmailField(max_length=100, unique=True)
    telephone=models.CharField(max_length=100, blank=True)

    # Character
    introduction=models.CharField(max_length=255, blank=True)
    personality=models.CharField(max_length=100, blank=True)
    religion=models.CharField(max_length=30, blank=True)

    # Physical description
    age=models.IntegerField(blank=True)
    height=models.CharField(max_length=5, blank=True)
    structure=models.CharField(max_length=30, blank=True)
    gender=models.CharField(max_length=30, blank=True)
    ethnicity=models.CharField(max_length=30, blank=True)
    language=models.CharField(max_length=30, blank=True)

    # Circumstance
    sexuality=models.CharField(max_length=30, blank=True)
    has_children=models.BooleanField(default=False)
    is_single=models.BooleanField(default=False)
    is_available=models.BooleanField(default=True)
    is_smoker=models.BooleanField(default=False)
    is_drinker=models.BooleanField(default=False)
    is_private=models.BooleanField(default=False)
    has_pets=models.BooleanField(default=False)
    living=models.CharField(max_length=30, blank=True)
    
    # achievements
    education=models.CharField(max_length=255, blank=True)
    career=models.CharField(max_length=255, blank=True)

    # socials
    facebook=models.CharField(max_length=255, blank=True)
    twitter=models.CharField(max_length=255, blank=True)
    instagram=models.CharField(max_length=255, blank=True)
    linkedin=models.CharField(max_length=255, blank=True)

    created_at=models.DateTimeField(auto_now_add=True)
    # update_at=models.DateTimeField(auto_now_add=False,blank=True)
    

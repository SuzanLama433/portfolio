from django.db import models

# Create your models here.
# models for contact
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
#models for project

class Project(models.Model):
    image = models.ImageField(upload_to='project_Image/')
    title = models.CharField(max_length=30)
    description = models.TextField()
    technologies = models.CharField(
        max_length=255,
        help_text="Separate technologies with commas"
    )
    live_demo= models.URLField(blank=True,null=True)
    github_link = models.URLField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text="Brief description of the project (max 1000 characters)")
    technologies = models.CharField(max_length=200, help_text="Arduino, C++, Python, React")

    # Links to code repository and live demo
    github_link = models.URLField()
    live_link = models.URLField(blank=True, null=True, help_text="Optional link to live demo"
    " or deployed project")
    
    # Image URL for project thumbnail(For now, later can be changed to ImageField if needed)
    image_url = models.URLField(help_text="Link to an image representing the project")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=2000, help_text="Your message (max 2000 characters)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

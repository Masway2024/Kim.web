from django.db import models

# Create your models here.

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Stores the timestamp when the message is created

    def __str__(self):
        return f"{self.name} - {self.subject}"

# models.py
from django.db import models

class WebsiteVisit(models.Model):
    visit_time = models.DateTimeField(auto_now_add=True)
    user_ip = models.CharField(max_length=100)  # Optionally store the user's IP address
    user_agent = models.CharField(max_length=255, blank=True)  # Optionally store user agent

    def __str__(self):
        return f"Visit on {self.visit_time} from {self.user_ip}"

# models.py
class CVDownload(models.Model):
    count = models.IntegerField(default=0)

    def increment_count(self):
        self.count += 1
        self.save()

    def __str__(self):
        return f"CV Downloads: {self.count}"

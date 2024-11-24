from django.db import models

# ContactMessages model
class ContactMessages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when message is created

    def __str__(self):
        return f"{self.name} - {self.subject}"


# WebsiteVisit model
class WebsiteVisit(models.Model):
    visit_time = models.DateTimeField(auto_now_add=True)
    user_ip = models.CharField(max_length=45)  # Adjusted for IPv4 and IPv6
    user_agent = models.CharField(max_length=255, blank=True)  # Optional user agent

    def __str__(self):
        return f"Visit on {self.visit_time} from {self.user_ip}"


# CVDownload model
class CVDownload(models.Model):
    count = models.IntegerField(default=0)

    def increment_count(self):
        self.count += 1
        self.save()

    def __str__(self):
        return f"CV Downloads: {self.count}"

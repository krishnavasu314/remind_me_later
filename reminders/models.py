from django.db import models

class Reminder(models.Model):
    REMINDER_METHODS = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]

    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    method = models.CharField(max_length=10, choices=REMINDER_METHODS)

    def __str__(self):
        return f"{self.method.capitalize()} reminder at {self.date} {self.time}"

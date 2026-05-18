from django.db import models


class Trip(models.Model):
    CLIMATE_CHOICES = [
        ('hot', 'Hot'),
        ('warm', 'Warm'),
        ('mild', 'Mild'),
        ('cold', 'Cold'),
    ]

    MEETING_CHOICES = [
        ('client', 'Client Meetings'),
        ('conference', 'Conference / Event'),
        ('internal', 'Internal Team'),
        ('mixed', 'Mixed'),
    ]

    destination = models.CharField(max_length=200)
    departure_date = models.DateField()
    return_date = models.DateField()
    climate = models.CharField(max_length=20, choices=CLIMATE_CHOICES)
    meeting_type = models.CharField(max_length=20, choices=MEETING_CHOICES)
    notes = models.TextField(blank=True, help_text="Any extra context (e.g. black tie dinner, outdoor site visit)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.destination} ({self.departure_date})"

    @property
    def duration_nights(self):
        return (self.return_date - self.departure_date).days

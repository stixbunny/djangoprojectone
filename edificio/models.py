from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", auto_now_add=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=5)
    location = models.CharField(max_length=200)
    image_url = models.URLField(null=True)
    description = models.CharField(max_length=500)
    floors = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(null=True)
    def __str__(self) -> str:
        return f"{self.name} - {self.pub_date.date().isoformat()}"

class ResidentialProperty(Property):
    type = models.CharField(max_length=50, default='residential')
    total_rooms = models.PositiveSmallIntegerField()

class IndustrialProperty(Property):
    type = models.CharField(max_length=50, default='industrial')
    industry = models.CharField(max_length=50)
    
class EntertainmentProperty(Property):
    type = models.CharField(max_length=50, default='entertainment')
    capacity = models.PositiveSmallIntegerField()

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import Min
# Create your models here.

class Apartment(models.Model):
    
    UNDERCONSTRUCTION_RESIDUAL = 'UNDER_CONSTRUCTION'
    READY_TO_MOVE = 'READY_TO_MOVE'
    COMPLETED_REAL_ESTATE = 'COMPLETED_REAL_ESTATE'
    COMMERCIAL = 'COMMERCIAL'
    PROJECT_CHOICES = [
        (UNDERCONSTRUCTION_RESIDUAL, 'Underconstruction project'),
        (READY_TO_MOVE, 'Ready to move project'),
        (COMPLETED_REAL_ESTATE, 'Completed real estate project'),
        (COMMERCIAL, 'Commercial'),
    ]
    name=models.CharField(max_length=200)
    # need to update amenities to checkbox
    amenities = models.CharField(max_length=300)
    specifications = models.TextField()
    address = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)    
    category = models.CharField(
        max_length=100,
        choices=PROJECT_CHOICES,
        default=UNDERCONSTRUCTION_RESIDUAL,
    )
    booking_status = models.CharField(
        max_length=10, 
        choices=[('OPEN', 'Open'),('CLOSED','Closed')])

    master_plan = models.ImageField(upload_to ='media/' ,default='img/layout/strip-foundation.jpg')
    floor_plan = models.ImageField(upload_to ='media/' ,default='img/layout/strip-foundation.jpg')
    tower_plan = models.ImageField(upload_to ='media/' ,default='img/layout/strip-foundation.jpg')


    def __str__(self):
        return self.name
    
    @property
    def min_price(self):
        return FlatTypes.objects.filter(apartment=self).values('price').aggregate(Min('price'))['price__min']
    
    @property
    def flat_type(self):
        flat_value = FlatTypes.objects.filter(apartment=self).values('flat_types')
        aggregated_flat_types=""
        for item in flat_value:
            aggregated_flat_types+=item["flat_types"][0]+"/"

        return aggregated_flat_types[:-1]


    class Meta:
        ordering = ['created_date']


class FlatTypes(models.Model):
    
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)    
    flat_types = models.CharField(max_length=200)
    price = models.IntegerField()


    def __str__(self):
        return self.apartment.name+" "+self.flat_types

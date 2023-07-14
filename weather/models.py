from django.db import models

class USCities(models.Model): 
    city=models.CharField(max_length=50) 
    state=models.CharField(max_length=50)
    temperature=models.IntegerField(blank=True, null=True)
    wind=models.IntegerField(blank=True, null=True)
    description=models.CharField(max_length=5, blank=True, null=True)
    icon=models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural='cities' 
        # ordering = ["id"]

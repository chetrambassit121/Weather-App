from django.db import models

class USCities(models.Model): 
    city=models.CharField(max_length=50, blank=True, null=True) 
    state=models.CharField(max_length=50, blank=True, null=True)
    temperature=models.IntegerField(blank=True, null=True)
    wind=models.IntegerField(blank=True, null=True)
    description=models.CharField(max_length=5, blank=True, null=True)
    icon=models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural='cities' 
        # ordering = ["id"]


# from django.db import models
# from gsheets import mixins
# from uuid import uuid4


# class USCities(mixins.SheetSyncableMixin, models.Model):
#     spreadsheet_id = '1_Rxr-2jkJgWmmO6xLJJ61SHEXeRCUVIgv6cXXnvz438'
#     model_id_field = 'guid'
#     guid = models.CharField(primary_key=True, max_length=255, default=uuid4)
#     city=models.CharField(max_length=50) 
#     state=models.CharField(max_length=50)
#     temperature=models.IntegerField(blank=True, null=True)
#     wind=models.IntegerField(blank=True, null=True)
#     description=models.CharField(max_length=5, blank=True, null=True)
#     icon=models.ImageField(null=True, blank=True)
    
#     def __str__(self):
#         return f'{self.city} // ({self.guid})'

#     class Meta:
#         verbose_name_plural='cities' 
#         # ordering = ["id"]
        


# print(USCities.sync_sheet())    
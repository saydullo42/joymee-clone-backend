from django.db import models
from account.models import CustomUser

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Country(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'countries'
        verbose_name_plural = 'Countries'
        ordering = ['name']

    def __str__(self):
        return self.name

class Region(BaseModel):
    country = models.ForeignKey(
        Country,
        related_name='regions',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'regions'
        ordering = ['name']

    def __str__(self):
        return self.name

class District(BaseModel):
    region = models.ForeignKey(
        Region,
        related_name='districts',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'districts'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} tumani ({self.region.name})"


class OwnerType(models.TextChoices):
    RIELTOR = 'rieltor', 'Rieltor'
    EGASI = 'egasi', 'Egasi'

class CurrencyType(models.TextChoices):
    UZS = 'uzs', "so'm"
    USD = 'usd', 'y.e'

class PropertyType(models.TextChoices):
    FLAT = 'flat', 'Flat'
    HOUSE = 'house', 'House'
    BUILDING = 'building', 'Building'
    LAND = 'land', 'Land'


class BaseProperty(BaseModel):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='properties'
    )
    property_type = models.CharField(
        max_length=30,
        choices=PropertyType.choices
    )
    title = models.CharField(max_length=255)
    body = models.TextField()
    main_image = models.ImageField(upload_to='images/property/')
    audio = models.FileField(upload_to='audio/property', null=True, blank=True)
    owner = models.CharField(
        max_length=20,
        choices=OwnerType.choices,
        default=OwnerType.RIELTOR
    )
    phone_number = models.CharField(max_length=20)
    is_credit = models.BooleanField(default=False)
    area = models.FloatField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(
        max_length=5,
        choices=CurrencyType.choices,
        default=CurrencyType.UZS
    )
    district = models.ForeignKey(
        District,
        related_name='properties',
        on_delete=models.PROTECT
    )

    class Meta:
        abstract = True








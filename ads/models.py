from django.db import models
from base.models import BaseProperty, BaseModel


class FlatType(models.TextChoices):
    NEW = 'yangi', 'Yangi bino'
    USED = "ikkinchi qo'l", "Ikkinchi qo'l"

class RepairType(models.TextChoices):
    KERAK = 'kerak', 'Kerak'
    KERAK_EMAS = 'kerak emas', 'Kerak emas'
    KOSMETIK = 'kosmetik', 'Kosmetik'
    YEVROREMONT = 'yevroremont', 'Yevroremont'
    DIZAYNERLIK = 'dizaynerlik', 'Dizaynerlik'


class Flat(BaseProperty):
    flat_type = models.CharField(
        max_length=20,
        choices=FlatType.choices,
        default=FlatType.NEW
    )
    repair_type = models.CharField(
        max_length=30,
        choices=RepairType.choices
    )
    room_count = models.PositiveIntegerField()
    floor_count = models.PositiveIntegerField()
    flat_floor_count = models.PositiveIntegerField()

    class Meta:
        db_table = 'flats'
        ordering = ['-created_at']

class FlatImage(BaseModel):
    flat = models.ForeignKey(
        Flat,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='images/flat/gallery/')

    class Meta:
        db_table = 'flat_images'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.flat.title} image"


class House(BaseProperty):
    repair_type = models.CharField(
        max_length=30,
        choices=RepairType.choices
    )
    house_floor_count = models.PositiveIntegerField()

    class Meta:
        db_table = 'houses'
        ordering = ['-created_at']

class HouseImage(BaseModel):
    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='images/house/gallery')

    class Meta:
        db_table = 'house_images'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.house.title} image"

class Building(BaseProperty):
    building_floor_count = models.PositiveIntegerField()

    class Meta:
        db_table = 'buildings'
        ordering = ['-created_at']

class BuildingImage(BaseModel):
    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='images/building/gallery')

    class Meta:
        db_table = 'building_images'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.building.title} image"

class Land(BaseProperty):
    class Meta:
        db_table = 'lands'
        ordering = ['-created_at']

class LandImage(BaseModel):
    land = models.ForeignKey(
        Land,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='images/land/gallery')

    class Meta:
        db_table = 'land_images'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.land.title} image"


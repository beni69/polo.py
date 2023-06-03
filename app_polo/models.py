from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=20, unique=True)
    hex = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f"{self.name} (#{self.hex})"

class Size(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    sizes = models.ManyToManyField(Size)
    colors = models.ManyToManyField(Color)
    link = models.URLField()
    image = models.URLField()

    def __str__(self):
        return self.name

class Class(models.Model):
    TYPES = [
            ("TAN", "Tanár"),
            ("OLD", "Öregdiák"),
            ("XA", "Leendő NYA"),
            ("XB", "Leendő 9B"),
            ("XC", "Leendő 9C"),
            ("XD", "Leendő 9D"),
            ("XE", "Leendő NYE"),
            ("XF", "Leendő NYF"),
            ("0A", "NYA"),
            ("0E", "NYE"),
            ("0F", "NYF"),
            ("9A", "9A"),
            ("9B", "9B"),
            ("9C", "9C"),
            ("9D", "9D"),
            ("9E", "9E"),
            ("9F", "9F"),
            ("10A", "10A"),
            ("10B", "10B"),
            ("10C", "10C"),
            ("10D", "10D"),
            ("10E", "10E"),
            ("10F", "10F"),
            ("11A", "11A"),
            ("11B", "11B"),
            ("11C", "11C"),
            ("11D", "11D"),
            ("11E", "11E"),
            ("11F", "11F"),
            ("12A", "12A"),
            ("12B", "12B"),
            ("12C", "12C"),
            ("12D", "12D"),
            ("12E", "12E"),
            ("12F", "12F"),
            ]
    
    type = models.CharField(
            max_length=3,
            choices=TYPES)

    teacher = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.type} ({self.teacher})" if self.teacher else str(self.type)

class PoloUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    osztaly = models.ForeignKey(Class, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.user.username} - {self.osztaly.type}"

class Order(models.Model):
    user = models.ForeignKey(PoloUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING)
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()

    def __str__(self):
        s = [f"{self.amount}db", self.size, self.color.name, self.product]
        return " ".join(str(x) for x in s if x)

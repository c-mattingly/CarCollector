from django.db import models
from django.urls import reverse

# Create your models here.
WORKS = (
    ('O', 'Oil Changed'),
    ('T', 'Tune Up'),
    ('R', 'Tire Rotation'),
)

class Part(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("parts_detail", kwargs={"pk": self.id})
    

class Car(models.Model):
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    comment = models.TextField(max_length=200)
    parts = models.ManyToManyField(Part)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse("detail", kwargs={'car_id': self.id})

class Maintenance(models.Model):
    date = models.DateField('maintenance date')
    work_done = models.CharField(
        max_length=1,
        choices=WORKS,
        default=[0][0]
    )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_work_done_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
    
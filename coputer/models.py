from django.db import models
from django.urls import reverse


class Cotegory(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.name


class Compyter(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField()
    price = models.IntegerField()
    genre = models.ManyToManyField(Cotegory)
    pamyat = models.FloatField(verbose_name='Pamyat operativniy')
    ekran = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    ozu = models.IntegerField()
    battery = models.IntegerField()

    @staticmethod
    def get_all_products():
        return Compyter.objects.all()

    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id:
            return Compyter.objects.filter(genre=category_id)
        else:
            return Compyter.objects.all()

    class Meta:
        db_table = 'Computer'

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

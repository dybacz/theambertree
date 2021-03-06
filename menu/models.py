from django.db import models

# Create your models here.#


class Group(models.Model):
    """"""

    name = models.CharField(max_length=128)
    friendly_name = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):
    """"""
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=128)
    friendly_name = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Item(models.Model):
    """"""
    group = models.ForeignKey('Group',
                              null=True,
                              blank=True,
                              on_delete=models.SET_NULL)
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8,
                                decimal_places=2,
                                null=True,
                                blank=True)
    rating = models.DecimalField(max_digits=4,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

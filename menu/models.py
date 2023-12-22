from django.db import models


class Menu(models.Model):
    nama_product = models.CharField(max_length=225)
    harga = models.IntegerField()
def __str__(self):
    return f"{self.nam_product}"

class formLogin(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.formLogin}"
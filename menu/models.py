from django.db import models
from django.utils.translation import ugettext_lazy as _


class Menu(models.Model):
    class TaskStatus(models.TextChoices):
       MENU = 'menu', _('Menu')
       IN_PROGRESS = 'in_progress', _('In progress')
       CLOSED = 'closed', _('Closed')  

    nama_product = models.CharField(max_length=225)
    harga = models.IntegerField()
    status = models.CharField(
       max_length=20, 
       choices=TaskStatus.choices,
       default=TaskStatus.MENU
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       db_table = 'Menu'

class formLogin(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.formLogin}"
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.

class Bayi(models.Model):
  # define status choices/options
  class BayiStatus(models.TextChoices):
    TODO = 'todo', _('Todo')
    IN_PROGRESS =  'in_progress', _('In Progress')
    CLOSED = 'closed', _('Closed')
  
  # define columns
  gender = (
    ('x', 'laki-laki'),
    ('y', 'perempuan'),
    )
  
  nama_bayi = models.CharField(max_length=100)
  jenis_kelamin = models.CharField(max_length=60, blank=True, default='',choices=gender,verbose_name="gender")
  umur = models.IntegerField()
  berat_badan = models.FloatField()
  tinggi_badan = models.FloatField()
  
  class Meta:
    # define table name
    db_table = 'bayis'
  
  
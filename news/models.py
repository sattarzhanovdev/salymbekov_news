from django.db import models

# Create your models here.

class News(models.Model):
  title = models.CharField(verbose_name='Название', max_length=20)
  description = models.TextField()
  image = models.ImageField(verbose_name='Фотография', upload_to='media/', null=True, blank=True)

  def __str__(self):
    return self.title

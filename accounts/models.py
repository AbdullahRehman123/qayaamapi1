from django.db import models
# Create your models here.
class Account(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(verbose_name='email', max_length = 254, unique=True)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    password = models.charField(max_length=100)
    type_choices = (
        ('Tenant', 'Tenant'),
        ('Realtor', 'Realtor'),
    )
    user_type = models.CharField(max_length=100, choices=type_choices, default='Tenant')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default='photo')
   
    def __str__(self):
        return self.name+" "+self.user_type

    def get_username(self):
        return self.email

        
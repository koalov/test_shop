from django.db import models

# Create your models here.


class Order(models.Model):
    order_date_time = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=150, verbose_name='Імʼя')
    order_phone = models.CharField(max_length=15, verbose_name='Телефон')

    def __str__(self):
        return f'{self.order_name} {self.order_phone}'

    def __repr__(self):
        return f'Order No: {self.pk}; Ordered by: {self.order_name}, ' \
               f'phone: {self.order_phone}'

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'


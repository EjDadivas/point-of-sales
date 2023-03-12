from django.db import models

# Create your models here.


class item(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    objects = models.Manager()

    def getPrice(self):
        return self.item_price

    def getName(self):
        return self.item_name

    def __str__(self):
        return str(self.pk) + ": " + self.item_name


class order(models.Model):
    total_amount_paid = models.DecimalField(max_digits=6, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    payment_type = models.CharField(max_length=100)
    objects = models.Manager()

    def getTotalAmountPaid(self):
        return self.total_amount_paid

    def getOrderDate(self):
        return self.order_date

    def getPaymentType(self):
        return self.payment_type

    def __str__(self):
        return str(self.pk) + ": " + self.order_date


class item_order(models.Model):
    item_id = models.ForeignKey(item, on_delete=models.PROTECT)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    line_total = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    objects = models.Manager()

    def getItemId(self):
        return self.item_id

    def getOrderId(self):
        return self.order_id

    def getLineTotal(self):
        return self.line_total

    def getQuantity(self):
        return self.quantity

    def __str__(self):
        return str(self.pk) + ": " + self.order_id

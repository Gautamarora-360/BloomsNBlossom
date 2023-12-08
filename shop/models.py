from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    Delivery_Information = models.CharField(max_length=500, default="")
    Product_Care = models.CharField(max_length=500, default="")
    
    publish_date = models.DateField(null=True)
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    query_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    query = models.CharField(max_length=500, default="")
    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000, default="")
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=20, default="")
    state = models.CharField(max_length=20, default="")
    zip_code = models.CharField(max_length=20, default="")
    # def __str__(self):
    #     return self.name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000, default="")
    timestamp = models.DateField(auto_now_add=True)
    # def __str__(self):
    #     return self.update_desc[0:10] + "..."

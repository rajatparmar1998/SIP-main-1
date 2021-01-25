from django.db import models

# Create your models here.

##class ForgetPassword(models.Model):
	##user_email = models.CharField(max_length=50, null=True, blank=True)
	##password = models.CharField(max_length=50, null=True, blank=True)
##	cnfpassword = models.CharField(max_length=50, null=True, blank=True)
  ##  class Meta:
    ##	db_table='user'

class category(models.Model):
	cat_id = models.BigAutoField(primary_key=True)
	cat_name = models.CharField(max_length=50, null=True, blank=True)
	class Meta:
		db_table = 'category'

	def __str__(self):
		return self.cat_name





class brand(models.Model):
	brand_id = models.BigAutoField(primary_key=True)
	brand_name = models.CharField(max_length=20, null=True, blank=True)

	class Meta:
		db_table = 'brand'

	def __str__(self):
		return self.brand_name

class product(models.Model):
	product_id = models.BigAutoField(primary_key=True)
	product_name = models.CharField(max_length=50, null=True, blank=True)
	#cat_name = models.CharField(max_length=50, null=True, blank=True)
	cat_id = models.ForeignKey(category, on_delete=models.CASCADE,null=True)
	brand_id = models.ForeignKey(brand, on_delete=models.CASCADE, null=True)

	#brand_name= models.CharField(max_length=20, null=True,blank=True)
	description = models.CharField(max_length=100, null=True, blank=True)
	price = models.IntegerField(null=True, blank=True)
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	image1 = models.ImageField(upload_to='images/', null=True, blank=True)
	stock = models.IntegerField(null=True, blank=True)
	class Meta:
		db_table= 'product'

	# def __str__(self):
	# 	return self.product_name, self.image, self.brand_id, self.cat_id, self.price

class addcart(models.Model):
	product_name = models.CharField(max_length=20,null=True)
	image = models.ImageField(upload_to='images/', null=True, blank=True)

	price = models.IntegerField(null=True, blank=True)

	class Meta:
		db_table = 'cart'


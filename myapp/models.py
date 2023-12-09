from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
class Category(models.Model):
    title=models.CharField(max_length=50)
    img=models.ImageField(upload_to='')
    slug=models.SlugField()
    def __str__(self):
        return self.title
class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    slug=models.SlugField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    img=models.ImageField(upload_to='')
    product_avaliable = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.title
class Cart(models.Model):
    cart_id=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    timestamp=models.DateTimeField(auto_now=True)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)

    def __str__(self):
        return self.product.title
    def update_quantity(self,quantity):
        self.quantity+=quantity
        self.save()
    def total(self):
        return self.quantity*self.price
class Buy(models.Model):
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.product.title+'_'+str(self.id)
class Reply(models.Model):      
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f"Reply by {self.user.username} on {self.product.title}"
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
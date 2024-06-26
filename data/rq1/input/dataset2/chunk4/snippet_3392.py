#Source: https://stackoverflow.com/questions/66828430/django-type-error-an-integer-is-required
from django.db import models
from django.conf import settings
from store.models import product, customer
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL
class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", default= None)
        qs = self.get_queryset().filter(id =cart_id)
        if qs.count()==1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj-save()
            else:
                cart_obj = cart.objects.new(user=request.user)
                new_obj = True
                request.session['cart_id'] = cart_obj.id
            return cart_obj, new_obj

    def new(self, user = None):
        user_obj = None
        if user is not None:
            if user is authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)

class cart(models.Model):
    user = models.ForeignKey(User, blank = True, null=True, on_delete=models.CASCADE)
    product = models.ManyToManyField('store.product')
    total = models.DecimalField(default = 0.0, max_digits = 50.00, decimal_places = 2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)
    objects = CartManager()

    def __str__(self):
        return str(self.id)
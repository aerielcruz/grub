from django.db.models import Model, ForeignKey, CASCADE, DateTimeField,  \
DateField, DecimalField, PositiveIntegerField, CharField, BooleanField,  \
PositiveSmallIntegerField

from django.contrib.auth.models import User

class Restaurant(Model):
    user = ForeignKey(User, on_delete=CASCADE, default=None, null=True)
    restaurant_name = CharField(max_length=191)
    street = CharField(max_length=191)
    zip_code = CharField(max_length=20, blank=True)
    state_or_province = CharField(max_length=191)
    country = CharField(max_length=191)
    telephone = CharField(max_length=191)
    
    created_at = DateField(auto_now_add=True, editable=False)
    deleted_at = DateTimeField(null=True, blank=True, editable=False)
    updated_at = DateField(auto_now=True, editable=False)

    def __str__(self):
	    return self.restaurant_name

class Dish(Model):
    user = ForeignKey(User, on_delete=CASCADE, default=None, null=True)
    dish_name = CharField(max_length=191)
    description = CharField(max_length=191)
    price = DecimalField('Php amount', max_digits=7, decimal_places=2, blank=True, null=True)
    restaurant = ForeignKey(Restaurant, on_delete=CASCADE, default=None, null=True, related_name='dishes')

    created_at = DateField(auto_now_add=True, editable=False)
    deleted_at = DateTimeField(null=True, blank=True, editable=False)
    updated_at = DateField(auto_now=True, editable=False)

    def __str__(self):
        return self.dish_name

class Review(Model):
    user = ForeignKey(User, on_delete=CASCADE, default=None, null=True)
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = CharField(max_length=191)

    created_at = DateField(auto_now_add=True, editable=False)
    deleted_at = DateTimeField(null=True, blank=True, editable=False)
    updated_at = DateField(auto_now=True, editable=False)
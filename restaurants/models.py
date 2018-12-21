from django.db.models import Model, ForeignKey, CASCADE, DateTimeField,  \
DecimalField, PositiveIntegerField, CharField, BooleanField,  \
PositiveSmallIntegerField, ImageField

from django.contrib.auth.models import User

class Category(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    category = CharField(max_length=191)
    is_active = BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class Restaurant(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=191)
    description = CharField(max_length=191)
    address = CharField(max_length=191)
    country = CharField(max_length=191)
    phone = CharField(max_length=191)
    category = ForeignKey(Category, on_delete=CASCADE)
    opening_hours = CharField(max_length=191)
    banner_image = ImageField(default='banner.jpg', upload_to='banner_image/%Y/%m/%d/', blank=True)
    
    created_at = DateTimeField(auto_now_add=True, editable=False)
    deleted_at = DateTimeField(null=True, blank=True, editable=False)
    updated_at = DateTimeField(auto_now=True, editable=False)

    def __str__(self):
	    return self.name


class Dish(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    dish = CharField(max_length=191)
    description = CharField(max_length=191)
    price = DecimalField('Php amount', max_digits=7, decimal_places=2, blank=True, null=True)
    restaurant = ForeignKey(Restaurant, on_delete=CASCADE)
    category = ForeignKey(Category, on_delete=CASCADE)

    created_at = DateTimeField(auto_now_add=True, editable=False)
    deleted_at = DateTimeField(null=True, blank=True, editable=False)
    updated_at = DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.dish


class Review(Model):
    RATING = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))

    user = ForeignKey(User, on_delete=CASCADE)
    rating = PositiveSmallIntegerField('Rating (stars)', blank=False, default=5, choices=RATING)
    comment = CharField(max_length=191)
    restaurant = ForeignKey(Restaurant, on_delete=CASCADE)

    created_at = DateTimeField(auto_now_add=True, editable=False)
    deleted_at = DateTimeField(null=True, blank=True, editable=False)
    updated_at = DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '{} | {} | {}'.format(self.user, self.restaurant, self.comment)
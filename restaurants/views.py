from django.shortcuts import render, redirect

from .forms import CategoryForm, RestaurantForm, DishForm, ReviewForm
from .models import Category, Restaurant, Dish, Review

from django.contrib.auth.decorators import login_required



def index(request):
    # Get data from the database
    # Output to html file

    # categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    context = {
        "title": "Restaurant List",
        # "categorylist": categories,
        "restaurantlist": restaurants,
    }

    return render(request, "restaurants/index.html", context)


@login_required
def create(request, category):
    if (category == "dish"):
        form = DishForm()
        if(request.method == "POST"):
            form = DishForm(request.POST)

            if form.is_valid():
                Dish.objects.create(
                    user = request.user,
                    dish = form.cleaned_data["dish"],
                    description = form.cleaned_data["description"],
                    price = form.cleaned_data["price"],
                    restaurant = form.cleaned_data["restaurant"],
                    category = form.cleaned_data["category"]
                    )
                return redirect("resto:success")
    elif (category == "restaurant"):
        form = RestaurantForm()
        if(request.method == "POST"):
            form = RestaurantForm(request.POST, request.FILES)

            if form.is_valid():
                Restaurant.objects.create(
                    user = request.user,
                    name = form.cleaned_data["name"],
                    address = form.cleaned_data["address"],
                    country = form.cleaned_data["country"],
                    phone = form.cleaned_data["phone"],
                    category = form.cleaned_data["category"],
                    opening_hours = form.cleaned_data["opening_hours"],
                    banner_image = form.cleaned_data["banner_image"]
                    )
                return redirect("resto:success")
    elif (category == "review"):
        form = ReviewForm()
        if(request.method == "POST"):
            form = ReviewForm(request.POST)

            if form.is_valid():
                Review.objects.create(
                    user = request.user,
                    rating = form.cleaned_data["rating"],
                    comment = form.cleaned_data["comment"],
                    restaurant = form.cleaned_data["restaurant"]
                    )
                return redirect("resto:success")

    context = {
		"form": form,
	}
    return render(request, "restaurants/create.html", context)


def read(request, category, id):
    if (category == "dish"):
        obj = Dish.objects.get(pk=id)
        title = obj.dish
        info = {
            "User": obj.user,
            "Dish": obj.dish,
            "Description": obj.description,
            "Price": obj.price,
            "Restaurant": obj.restaurant,
            "Category": obj.category,
            "Created at": obj.created_at,
            "Updated at": obj.updated_at,
        }
    else:
        obj = Restaurant.objects.get(pk=id)
        title = obj.name
        info = {
            "User": obj.user,
            "Name": obj.name,
            "Address": obj.address,
            "Country": obj.country,
            "Phone": obj.phone,
            "Category": obj.category,
            "Opening hours": obj.opening_hours,
            "Banner image": obj.banner_image,
            "Created at": obj.created_at,
            "Updated at": obj.updated_at,
        }    

    resto = Restaurant.objects.get(pk=id)
    dishes = Dish.objects.filter(restaurant=resto)
    reviews = Review.objects.filter(restaurant=resto)

    # categories = dishes.objects.filter(category=category)

    context = {
		"title": title,
		"obj": obj,
		"info": info,
        "dishlist": dishes,
        "reviewlist": reviews
	}
    return render(request, "restaurants/read.html", context)

@login_required
def update(request, category, id):
    if (category == "dish"):
        obj = Dish.objects.get(pk=id)
        form = DishForm(instance=obj)

        if (request.method == "POST"):
            form = DishForm(request.POST)

            if form.is_valid():
                Dish.objects.filter(pk=id).update(
                    dish = form.cleaned_data["dish"],
                    description = form.cleaned_data["description"],
                    price = form.cleaned_data["price"],
                    restaurant = form.cleaned_data["restaurant"],
                    category = form.cleaned_data["category"]
                    ) 
                return redirect("resto:index")
    else:
        obj = Restaurant.objects.get(pk=id)
        form = RestaurantForm(instance=obj)

        if (request.method == "POST"):
            form = RestaurantForm(request.POST)

            if form.is_valid():
                Restaurant.objects.filter(pk=id).update(
                    name = form.cleaned_data["name"],
                    address = form.cleaned_data["address"],
                    country = form.cleaned_data["country"],
                    phone = form.cleaned_data["phone"],
                    category = form.cleaned_data["category"],
                    opening_hours = form.cleaned_data["opening_hours"]
                    ) 
                return redirect("resto:index")
                
    context = {
        "form": form,
    }
    return render(request, "restaurants/create.html", context)


@login_required
def delete(request, category, id):
    if (category == "dish"):
        Dish.objects.get(pk=id).delete()
        return redirect("resto:deleted")
    else:
        Restaurant.objects.get(pk=id).delete()
        return redirect("resto:deleted")

def deleted(request):
	return render(request, "restaurants/deleted.html")

def success(request):
	return render(request, "success.html")
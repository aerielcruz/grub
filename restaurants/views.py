from django.shortcuts import render, redirect

from .forms import CategoryForm, RestaurantForm, DishForm, ReviewForm
from .models import Category, Restaurant, Dish, Review

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    # Get data from the database
    # Output to html file

    # categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    # dishes = Dish.objects.all()
    context = {
        "title": "Restaurant List",
        # "categorylist": categories,
        "restaurantlist": restaurants,
        # "dishlist": dishes
    }

    return render(request, "restaurants/index.html", context)


@login_required
def create(request):
    form = RestaurantForm()
    
    if(request.method == "POST"):
        form = RestaurantForm(request.POST)

        if form.is_valid():
            Restaurant.objects.create(
                user = request.user,
                name = form.cleaned_data["name"],
                address = form.cleaned_data["address"],
                country = form.cleaned_data["country"],
                phone = form.cleaned_data["phone"],
                category = form.cleaned_data["category"],
                opening_hours = form.cleaned_data["opening_hours"]
                )
            return redirect("resto:success")
    
    context = {
		"form": form,
	}
    return render(request, "restaurants/create.html", context)


def read(request, id):
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
        "Created at": obj.created_at,
		"Updated at": obj.updated_at,
    }
	
    context = {
		"title": title,
		"obj": obj,
		"info": info,
	}
    return render(request, "restaurants/read.html", context)

@login_required
def update(request, id):
    obj = Restaurant.objects.get(pk=id)
    form = RestaurantForm(instance=obj)

    if (request.method == "POST"):
        form = RestaurantForm(request.POST)

        if form.is_valid():
            # user = request.user,
            # name = form.cleaned_data["name"],
            # address = form.cleaned_data["address"],
            # country = form.cleaned_data["country"],
            # phone = form.cleaned_data["phone"],
            # category = form.cleaned_data["category"],
            # opening_hours = form.cleaned_data["opening_hours"]


            # # obj = Restaurant()
            # # obj.user = user
            # # obj.user = request.user
            # obj.name = name
            # obj.address = address
            # obj.country = country
            # obj.phone = phone
            # obj.category = category
            # obj.opening_hours = opening_hours
            # obj.save()

            Restaurant.objects.filter(pk=id).update(
                # user = request.user,
                name = form.cleaned_data["name"],
                address = form.cleaned_data["address"],
                country = form.cleaned_data["country"],
                phone = form.cleaned_data["phone"],
                category = form.cleaned_data["category"],
                opening_hours = form.cleaned_data["opening_hours"]
                ) 

            # Restaurant.objects.create(
            #     user = request.user,
            #     name = form.cleaned_data["name"],
            #     address = form.cleaned_data["address"],
            #     country = form.cleaned_data["country"],
            #     phone = form.cleaned_data["phone"],
            #     category = form.cleaned_data["category"],
            #     opening_hours = form.cleaned_data["opening_hours"]
            #     )

            return redirect("resto:index")
                
    context = {
        "form": form,
    }
    return render(request, "restaurants/create.html", context)

def success(request):
	return render(request, "success.html")
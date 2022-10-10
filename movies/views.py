from django.shortcuts import render, redirect
from .forms import MovieForm, ReviewForm
from .models import Movie, Review


def index(request):
    reviews = Review.objects.all()

    context = {"reviews": reviews}

    return render(request, "movies/index.html", context)


def create(request):
    if request.method == "POST":
        form_R = ReviewForm(request.POST)
        if form_R.is_valid():
            form_R.save()
            return redirect("movies:index")
    else:
        form_R = ReviewForm()
    context = {"form_R": form_R}

    return render(request, "movies/create.html", context)


def delete(reuqest, pk):
    Review.objects.get(pk=pk).delete()

    return redirect("movies:index")


def search(request):
    search = request.GET.get("search", "")

    if request.GET.get("keyword") == "1":
        reviews = Review.objects.filter(title__icontains=search)

    elif request.GET.get("keyword") == "2":
        reviews = Review.objects.filter(content__icontains=search)
    else:
        #  request.GET.get("keyword") == 3:
        reviews = Review.objects.filter(movie_name__icontains=search)

    context = {"reviews": reviews}

    return render(request, "movies/index.html", context)


# Create your views here.

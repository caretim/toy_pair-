from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import MovieForm, ReviewForm
from .models import Movie, Review

# Create your views here.


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
    Movie.objects.get(pk=pk).delete()

    return redirect("movies:movie_info")


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


def movie_info(request):
    movies = Movie.objects.all()
    context = {"movies": movies}
    return render(request, "movies/movie_info.html", context)


def movie_create(request):
    if request.method == "POST":
        form_M = MovieForm(request.POST)
        if form_M.is_valid():
            form_M.save()
            return redirect("movies:movie_info")
    else:
        form_M = MovieForm()
    context = {"form_M": form_M}

    return render(request, "movies/movie_create.html", context)


def genre_search(request, genre):
    genre = genre
    movies = Movie.objects.filter(genre=genre)
    context = {"movies": movies}
    return render(request, "movies/movie_info.html", context)


def movie_detail(request, pk):
    k = Movie.objects.get(pk=pk)
    j = k.movie_title
    context = {
        "movie": k,
    }
    return render(request, "movies/movie_detail.html", context)


def movie_update(request, pk):
    k = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form_R = MovieForm(request.POST, instance=k)
        if form_R.is_valid():
            form_R.save()
            return redirect("/", k.pk)
    else:
        form_R = MovieForm(instance=k)
    context = {
        "form_R": form_R,
        "j": k,
    }

    return render(request, "movies/movie_update.html", context)

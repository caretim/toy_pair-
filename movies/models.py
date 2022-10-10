from django.db import models

# Create your models here.
RATE_CHOICES = (
    (1, "★"),
    (2, "★★"),
    (3, "★★★"),
    (4, "★★★★"),
    (5, "★★★★★"),
)

class Review(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    movie_name = models.CharField(max_length=30)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    grade = models.IntegerField(choices=RATE_CHOICES)

    # 글씨 갯수 그건 테이블 갯수의 문제지
    # 장르의 이름의 길이는 상관이 없음


genre_table = (
    ("액션", "액션"),
    ("스릴러", "스릴러"),
    ("코미디", "코미디"),
    ("로맨스", "로맨스"),
    ("SF", "SF"),
    ("드라마", "드라마"),
    ("애니메이션", "애니메이션"),
)

class Movie(models.Model):
    movie_title = models.CharField(max_length=30)
    summary = models.TextField()
    genre = models.CharField(max_length=80,choices=genre_table)
    start_at = models.DateField()

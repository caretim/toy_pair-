from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    movie_name = models.CharField(max_length=30)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # 글씨 갯수 그건 테이블 갯수의 문제지
    # 장르의 이름의 길이는 상관이 없음


class Movie(models.Model):
    movie_title = models.CharField(max_length=30)
    summary = models.TextField()
    genre = models.CharField(max_length=80)
    start_at = models.DateField()

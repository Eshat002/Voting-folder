from django.urls import path
from question import views

urlpatterns = [
    path('', views.home),
    path('get-questions/<int:dyna_visible_questions>/', views.questions_view),
    path('vote/', views.vote_view),
]

"""
URL configuration for rest_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from games import views
from scraper import views as scraper_views

urlpatterns = [
    path('baseball_games_today/', views.baseball_games_today, name='baseball_today'),

    path('basketball_games_today/', views.basketball_games_today, name='basketball_today'),

    path('football_games_today/', views.football_games_today, name='football_today'),

    path('twitter_scraper/<str:away>/<str:home>/', scraper_views.scrape_twitter),
    path('ame_football_games_today/<int:league>/', views.ame_football_games_today, name='ame_football_today'),

    path('admin/', admin.site.urls),
]

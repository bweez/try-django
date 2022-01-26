"""tryDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path

from .views import home_view
from articles.views import (
    article_search_view,
    article_create_view,
    article_details_view
)
from accounts.views import (
    login_view,
    logout_view,
    register_view
)


# order matter in this url patterns
# path('articles/create/', article_views.article_create_view),
# path('articles/<str:id>', article_views.article_details_view),
# if these 2 were switched "create" would be interperted as an :id value
urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('articles/', article_search_view),
    path('articles/create/', article_create_view),
    # how to dynamically add the id str
    path('articles/<str:id>', article_details_view),
    # re_path(r'articles/(?P<id>\d+/$', home_view),  # alternate pathing with a regex
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
]

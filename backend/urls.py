"""dvdnp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path, re_path
from rest_framework import routers

from .api.views import CommentViewSet, VueTemplateView

router = routers.DefaultRouter()
router.register("comments", CommentViewSet)

urlpatterns = [
    # Django admin page
    path("admin/", admin.site.urls),
    # Api ViewSet
    path("api/", include(router.urls)),
    # Vue template view that is served in the production environment
    re_path(r"^.*$", VueTemplateView.as_view(), name="entry_point"),
]

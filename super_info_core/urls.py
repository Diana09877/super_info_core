"""
URL configuration for super_info_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from blog.views import HomeView, PublicationDetailView, PublicationCommentsView, HomeSearchView, \
    Contact_view
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),

]


urlpatterns += i18n_patterns(
    path('', HomeView.as_view(), name='home'),
    path('home/search/', HomeSearchView.as_view(), name='home-search-url'),
    path('publication-detail/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail-url'),
    path('publication-detail/<int:pk>/create-comment/', PublicationCommentsView.as_view()),
    path('contact/', Contact_view, name='contact'),
)



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



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
from django.contrib import admin
from blog.views import HomeView, PublicationDetailView, PublicationCommentsView, ContactView, HomeSearchView, \
    Contact_view
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('home/search/', HomeSearchView.as_view(), name='home-search-url'),
    path('publication-detail/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail-url'),
   # path('publication-detail/related-publications/<int:pk>/', RelatedPublicationsView.as_view(),),
    path('publication-detail/', PublicationDetailView.as_view(), name='publication-detail'),
    #path('publication-detail/', CategoriesView.as_view(), name='categories'),
    #path('publication-detail/<int:pk>/',PublicationCommentView.as_view(), name='publications'),
    path('publication-detail/<int:pk>/create-comment/', PublicationCommentsView.as_view()),
    path('contact/', Contact_view, name='contact')



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


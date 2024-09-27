from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from blog.models import Publication, Category,PublicationComment
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        publications = Publication.objects.filter(is_active=True)

        paginator = Paginator(publications,3)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj

        }
        return context

class HomeSearchView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        search_word = self.request.GET.get('search','')
        publications = Publication.objects.filter(is_active=True).filter(
                Q(title__icontains=search_word) | Q(short_description__icontains=search_word) |
                Q(full_description__icontains=search_word) | Q(category__title__icontains=search_word) |
                Q(hashtags__title__icontains=search_word)
            )
        paginator = Paginator(publications, 3)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj

        }
        return context


class PublicationDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        publication_id = self.kwargs.get('pk')
        publication = get_object_or_404(Publication, id=publication_id)
        related_publications = Publication.objects.exclude(id=publication_id)[:3]

        context = {
            'publication': publication,
            'related_publications': related_publications,
            'category_list': Category.objects.all(),
        }

        return render(request, 'publication-detail.html', context)


class PublicationCommentsView(View):

    def post(self, request, *args, **kwargs):
        publication_pk = kwargs['pk']
        publication = Publication.objects.get(id=publication_pk)
        comment_text = request.POST['comment_text']
        author_name = request.POST['author_name']

        PublicationComment.objects.create(publication=publication, comment_text=comment_text, author_name=author_name)
        #bot.send_message(bot=telebot.TeleBot(chat_id), text='CHECK IT OUT! comment has been written for your publucation.')
        return redirect('publication-detail-url', pk=publication_pk)

def Contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        return HttpResponse("Спасибо за ваше сообщение!")
    return render(request, 'contact.html')

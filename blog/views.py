# from django.shortcuts import render, redirect, get_object_or_404
import telebot
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from blog.models import Publication, Category,PublicationComment
from django.shortcuts import render, redirect



class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        publications = Publication.objects.filter(is_active=True)

        paginator = Paginator(publications,3)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj

        }
        return context

class HomeSearchView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        search_word = self.request.GET['search']
        context = {
            'page_obj': Publication.objects.filter(is_active=True).filter(
                Q(title__icontains=search_word) | Q(description__icontains=search_word)
            )
        }
        return context

class PublicationDetailView(TemplateView):
    template_name = 'publication-detail.html'
    def get_context_data(self,  **kwargs):
        publication_pk = kwargs['pk']
        context = {
            
            'publication': Publication.objects.get(id=publication_pk),
            'related_publications': Publication.objects.filter(is_active=True).exclude(id=publication_pk),
            'category_list': Category.objects.all(),

        }
        return context
#
# class RelatedDetailView(TemplateView):
#     template_name = 'publication-detail.html'
#     def get_context_data(self, **kwargs):
#        publication_pk = kwargs['pk'],
#        related_publications = Publication.objects.filter(is_active=True).exclude(id=publication_pk),
#
#        context = {
#            'related_publications': related_publications
#
#        }
#        return context



# class RelatedPublicationsView(View):
#     template_name = 'publication-detail.html'
#
#     def get_context_data(self, **kwargs):
#         publication_pk = kwargs['pk']
#         context = {
#             'related_publications': Publication.objects.filter(is_active=True).exclude(id=publication_pk),
#
#         }
#         return context
#
# class CategoriesView(TemplateView):
#     template_name = 'publication-detail.html'
#     def get_context_data(self, **kwargs):
#         context = {
#             'category_list': Category.objects.all(),
#         }
#         return context

    # def publication_list(request):
    #     publications = Publication.objects.filter(is_active=True)
    #     return render(request, 'index.html', {'publications': publications})
    #
    # def post_detail(request, pk):
    #     publication = get_object_or_404(Publication, pk=pk)
    #     return render(request, 'publication-detail.html', {'publication': publication})




# class CommentView(TemplateView):
#     template_name = 'publication-detail.html'
#
#     def get_context_data(self, *args, **kwargs):
#          context = {
#              'comments': Comment.objects.all()
#
#         }
#          return context
# #




class PublicationCommentsView(View):
    def post(self, request, *args, **kwargs):
        publication_pk = kwargs['pk']
        publication = Publication.objects.get(id=publication_pk)
        comment_text = request.POST['comment_text']
        author_name = request.POST['author_name']

        PublicationComment.objects.create(publication=publication, comment_text=comment_text, author_name=author_name)
        bot.send_message(bot=telebot.TeleBot(chat_id=6512041910), text='CHECK IT OUT! comment has been written for your publucation.')
        return redirect('publication-detail-url', pk=publication_pk)
#
# class ContactView(TemplateView):
#     template_name = 'contact.html'
#
#     def get_context_data(self, **kwargs):
#         context = {
#             'contact_us': Comment.objects.first()
#         }
#         return context
#
#     def post(self, request, **kwargs):
#         publication_pk = kwargs['pk']
#         publication = Publication.objects.get(id=publication_pk)
#         commant_text = request.POST['comment_text']
#         PublicationComment.objects.create(publication=publication, text=commant_text)
#         bot.send_message(chat_id=6512041910, text='CHECK IT OUT! comment has been written for your publucation.')
#         return render('publication-detail.html', publication_pk),


def Contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        return HttpResponse("Спасибо за ваше сообщение!")
    return render(request, 'contact.html')

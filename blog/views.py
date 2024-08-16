# from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from blog.models import Publication, Category,PublicationComment
from django.shortcuts import render, redirect

from blog.telegram_bot import bot


class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = {
            'publication_list': Publication.objects.filter(is_active=True)
        }
        return context

class HomeSearchView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        search_word = self.request.GET['search']
        context = {
            'publication_list': Publication.objects.filter(is_active=True, title_icontains=search_word)
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

        PublicationComment.objects.create(publication=publication, text=comment_text)
        bot.send_message(chat_id=2, text='CHECK IT OUT! comment has been written for your publucation.')
        return redirect('publication-detail', pk=publication_pk)

class ContactView(TemplateView):
    template_name = 'contact.html'

# class PublicationCommentView(TemplateView):
#     template_name = 'publication-detail'
#     def get_context_data(self, **kwargs):
#         context = {
#             'publications': Publication.objects.all()
#         }
#         return context


def Contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        return HttpResponse("Спасибо за ваше сообщение!")
    return render(request, 'contact.html')

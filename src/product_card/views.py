from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from . import models, forms
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

class ShowProductCardList(generic.ListView):
    login_url = 'home_page:login'
    permission_required = 'product_card.view_book'
    model = models.Book
    template_name = 'product_card/list_pc.html'


class ShowProductCard(generic.DetailView):
    login_url = 'home_page:login'
    permission_required = 'product_card.view_book'
    model = models.Book
    template_name = 'product_card/detail_pc.html'


class CreateProductCard(generic.CreateView):
    login_url = 'home_page:login'
    permission_required = 'product_card.add_book'
    model = models.Book
    form_class = forms.ProductCardForm
    template_name = 'product_card/edit_pc.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context


class UpdateProductCard(generic.UpdateView):
    login_url = 'home_page:login'
    permission_required = 'product_card.change_book'
    model = models.Book
    form_class = forms.ProductCardForm
    template_name = 'product_card/edit_pc.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context


class DeleteProductCard(generic.DeleteView):
    login_url = 'home_page:login'
    permission_required = 'product_card.delete_book'
    model = models.Book
    template_name = 'product_card/delete_pc.html'

    def get_success_url(self):
        return reverse_lazy('product_card:pc_list')
    

class SearchResultView(generic.View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        results = ''
        if query:
            results = models.Book.objects.filter(
                Q(author__name__icontains=query) | Q(name__icontains=query) | Q(author__surname__icontains=query)
            ).distinct()
        paginator = Paginator(results, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'product_card/search.html', context={
            'title': 'Search',
            'results': page_obj,
            'count': paginator.count,
        })

class BookDetail(generic.DetailView):


    def get(self, request, *args, **kwargs):
        book = get_object_or_404(models.Book, pk=kwargs['pk'])
        last_posts = models.Book.objects.all().order_by('-id')[:3]

        return render(request, 'product_card/book_detail.html', context={
            'book': book,
        }) 
    

class CatalogView(generic.View):

    def get(self, request, *args, **kwargs):
        book = models.Book.objects.all()
        paginator = Paginator(book, 12)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'product_card/catalog.html',
            context={
                'page_obj': page_obj
            }
        )
    

class PortalView(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        return render(
            request, 'product_card/portal_detail.html'
        )
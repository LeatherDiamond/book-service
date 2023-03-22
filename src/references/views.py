from django.shortcuts import render
from django.views import generic
from references import models, forms
from django.urls import reverse_lazy

# Create your views here.


#CBV for Author model.

class ShowAuthors(generic.ListView):
    login_url = 'home_page:login'
    permission_required = 'references.view_bookauthor'
    model = models.BookAuthor
    template_name = 'references/list_author.html'


class ShowAuthor(generic.DetailView):
    model = models.BookAuthor
    login_url = 'home_page:login'
    permission_required = 'references.view_bookauthor'
    template_name = 'references/detail_author.html'


class CreateAuthor(generic.CreateView):
    login_url = 'home_page:login'
    permission_required = 'references.add_bookauthor'
    model = models.BookAuthor
    form_class = forms.AuthorForm
    template_name = 'references/edit_author.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context


class UpdateAuthor(generic.UpdateView):
    login_url = 'home_page:login'
    permission_required = 'references.change_bookauthor'
    model = models.BookAuthor
    form_class = forms.AuthorForm
    template_name = 'references/edit_author.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context


class DeleteAuthor(generic.DeleteView):
    login_url = 'home_page:login'
    permission_required = 'references.delete_bookauthor'
    model = models.BookAuthor
    template_name = 'references/delete_author.html'

    def get_success_url(self):
        return reverse_lazy('references:authors_list')

#CBV for Series model.

class ShowAllSeries(generic.ListView):
    login_url = 'home_page:login'
    permission_required = 'references.view_bookseries'
    model = models.BookSeries
    template_name = 'references/list_series.html'


class ShowSeries(generic.DetailView):
    login_url = 'home_page:login'
    permission_required = 'references.view_bookseries'
    model = models.BookSeries
    template_name = 'references/detail_series.html'


class CreateSeries(generic.CreateView):
    login_url = 'home_page:login'
    permission_required = 'references.add_bookseries'
    model = models.BookSeries
    form_class = forms.SeriesForm
    template_name = 'references/edit_series.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context


class UpdateSeries(generic.UpdateView):
    login_url = 'home_page:login'
    permission_required = 'references.change_bookseries'
    model = models.BookSeries
    form_class = forms.SeriesForm
    template_name = 'references/edit_series.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context


class DeleteSeries(generic.DeleteView):
    login_url = 'home_page:login'
    permission_required = 'references.delete_bookseries'
    model = models.BookSeries
    template_name = 'references/delete_series.html'

    def get_success_url(self):
        return reverse_lazy('references:series_list')

#CBV for Genre model.

class ShowGenres(generic.ListView):
    login_url = 'home_page:login'
    permission_required = 'references.view_bookgenre'
    model = models.BookGenre
    template_name = 'references/list_genre.html'


class ShowGenre(generic.DetailView):
    login_url = 'home_page:login'
    permission_required = 'references.view_bookgenre'
    model = models.BookGenre
    template_name = 'references/detail_genre.html'


class CreateGenre(generic.CreateView):
    login_url = 'home_page:login'
    permission_required = 'references.add_bookgenre'
    model = models.BookGenre
    form_class = forms.GenreForm
    template_name = 'references/edit_genre.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context


class UpdateGenre(generic.UpdateView):
    login_url = 'home_page:login'
    permission_required = 'references.change_bookgenre'
    model = models.BookGenre
    form_class = forms.GenreForm
    template_name = 'references/edit_genre.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context


class DeleteGenre(generic.DeleteView):
    login_url = 'home_page:login'
    permission_required = 'references.delete_bookgenre'
    model = models.BookGenre
    template_name = 'references/delete_genre.html'

    def get_success_url(self):
        return reverse_lazy('references:genres_list')

#CBV Publishing house form.

class ShowHouses(generic.ListView):
    login_url = 'home_page:login'
    model = models.BookPublishingHouse
    template_name = 'references/list_house.html'


class ShowHouse(generic.DetailView):
    login_url = 'home_page:login'
    permission_required = 'references.view_bookpublishinghouse'
    model = models.BookPublishingHouse
    template_name = 'references/detail_house.html'


class CreateHouse(generic.CreateView):
    login_url = 'home_page:login'
    permission_required = 'references.add_bookpublishinghouse'
    model = models.BookPublishingHouse
    form_class = forms.PublishingHouseForm
    template_name = 'references/edit_house.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context


class UpdateHouse(generic.UpdateView):
    login_url = 'home_page:login'
    permission_required = 'references.change_bookpublishinghouse'
    model = models.BookPublishingHouse
    form_class = forms.PublishingHouseForm
    template_name = 'references/edit_house.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context


class DeleteHouse(generic.DeleteView):
    login_url = 'home_page:login'
    permission_required = 'references.delete_bookpublishinghouse'
    model = models.BookPublishingHouse
    template_name = 'references/delete_house.html'

    def get_success_url(self):
        return reverse_lazy('references:houses_list')
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from materials.models import Materials


class MaterialsCreateView(CreateView):
    model = Materials
    fields = ('title', 'body',)
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid:
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class MaterialsUpdateView(UpdateView):
    model = Materials
    fields = ('title', 'body',)
    success_url = reverse_lazy('materials:list')


class MaterialsListView(ListView):
    model = Materials

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset


class MaterialsDetailView(DetailView):
    model = Materials

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        return self.object


class MaterialsDeleteView(DeleteView):
    model = Materials
    success_url = reverse_lazy('materials:list')

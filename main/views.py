from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Student


class StudentListView(ListView):
    model = Student


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f'Имя - {name} email({email}): сообщение({message})')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'main/contact.html', context)


class StudentDetailsView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('main:index')


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('main:index')


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('main:index')


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_activ:
        student_item.is_activ = False
    else:
        student_item.is_activ = True

    student_item.save()

    return redirect(reverse('main:index'))

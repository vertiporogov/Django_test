from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from main.models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Главная'
    }

# def index(request):
#     students_list = Student.objects.all()
#
#     context = {
#         'object_list': students_list,
#         'title': "Главная",
#     }
#
#     return render(request, 'main/index.html', context)




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
    template_name = "main/student_detail.html"

# def view_student(request, pk):
#     student_item = get_object_or_404(Student, pk=pk)
#     context = {
#         'object': student_item,
#     }
#     return render(request, "main/student_detail.html", context)


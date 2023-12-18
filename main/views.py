from django.shortcuts import render

from main.models import Student


def index(request):
    students_list = Student.objects.all()

    context = {
        'object_list': students_list,
        'title': "Главная",
    }

    return render(request, 'main/index.html', context)

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

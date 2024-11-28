from django.shortcuts import render

from students.models import Student


def example_data(request):
    return render(request, 'app/example.html')


def show_data(request):
    if request.method == 'GET':
        return render(request, 'app/show_data.html')


def submit_data(request):
    if request.method == 'POST':
        return render(request, 'app/submit_data.html')


def show_item(request, item_id):
    return render(request, 'app/item/html', {'item_id': item_id})


def example_view(request):
    return render(request, 'students/example.html')


def index(request):
    student = Student.objects.get(id=1)
    context = {
        'student_name': f'{student.first_name} {student.last_name}',
        'student_year': student.get_year_display(),
    }
    return render(request, 'students/index.html', context=context)


def student_detail(request, student):
    student = Student.objects.get(id=1)
    context = {
        'student': student,
    }
    return render(request, 'students/student_detail.html', context=context)


def student_list(request):
    student_list = Student.objects.all()
    context = {
    'students': student_list
    }
    return render(request, 'students/student_list.html', context=context)
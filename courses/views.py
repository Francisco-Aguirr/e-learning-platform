from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import EnrollmentForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.course = course
            enrollment.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = EnrollmentForm()

    return render(request, 'course_detail.html', {
        'course': course,
        'form': form
    })

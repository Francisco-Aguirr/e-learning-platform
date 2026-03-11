from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollment, Lesson
from .forms import EnrollmentForm
from django.contrib import messages


def course_list(request):
    courses = Course.objects.all()

    for course in courses:
        course.student_count = course.enrollment_set.count()

    return render(request, 'course_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrollments = Enrollment.objects.filter(course=course)
    lessons = course.lessons.all().order_by('order')

    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['student_name']

            existing_enrollment = Enrollment.objects.filter(
        course=course,
        student_name=student_name
    ).first()
            if not existing_enrollment:
                enrollment = form.save(commit=False)
                enrollment.course = course
                enrollment.save()
                messages.success(request, "You have successfully enrolled in this course!")
            else:
                messages.warning(request, "You are already enrolled in this course.")
                return redirect('course_detail', course_id=course.id)
    else:
        form = EnrollmentForm()

    return render(request, 'course_detail.html', {
        'course': course,
        'form': form,
        'enrollments': enrollments,
        'lessons': lessons
    })

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})
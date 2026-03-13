from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollment, Lesson, LessonCompletion
# from .forms import EnrollmentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


def course_list(request):
    courses = Course.objects.order_by('-created_at')

    for course in courses:
        course.student_count = course.enrollment_set.count()

    return render(request, 'course_list.html', {'courses': courses})


def course_detail(request, course_id):

    course = get_object_or_404(Course, id=course_id)

    lessons = course.lessons.all().order_by('order')

    enrollments = Enrollment.objects.filter(course=course)

    # Handle enrollment
    if request.method == "POST":

        if request.user.is_authenticated:

            Enrollment.objects.get_or_create(
                user=request.user,
                course=course
            )

            messages.success(request, "You are now enrolled in this course!")

        else:

            messages.warning(request, "You must log in to enroll in this course.")

        return redirect('course_detail', course_id=course.id)

    # Calculate progress
    total_lessons = lessons.count()
    completed_lessons = 0
    progress = 0

    if request.user.is_authenticated:

        completed_lessons = LessonCompletion.objects.filter(
            user=request.user,
            lesson__course=course
        ).count()

        if total_lessons > 0:
            progress = int((completed_lessons / total_lessons) * 100)

    return render(request, 'course_detail.html', {
        'course': course,
        'enrollments': enrollments,
        'lessons': lessons,
        'progress': progress
    })

@login_required
def lesson_detail(request, lesson_id):

    lesson = get_object_or_404(Lesson, id=lesson_id)

    # Mark lesson as completed
    LessonCompletion.objects.get_or_create(
        user=request.user,
        lesson=lesson
    )

    return render(request, 'lesson_detail.html', {
        'lesson': lesson
    })

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {
        'form': form
    })

from .models import Course

def home(request):

    courses = Course.objects.all().order_by('-created_at')[:3]

    return render(request, 'home.html', {
        'courses': courses
    })
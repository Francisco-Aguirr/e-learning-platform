# E-Learning Platform

# Overview
This project is a web-based learning management system built to deepen my understanding of full-stack web development with Django. The application allows users to browse courses, view lessons, track their progress, and enroll in courses. It demonstrates key web development concepts such as user authentication, database relationships, dynamic content rendering, and form handling.

The application is designed to be a simple yet functional prototype of an online course platform. Users can sign up, log in, view a list of available courses, see detailed course information including lessons, and enroll. The progress bar on each course page gives a visual indication of how many lessons the user has completed (based on a simplified model).

To run the project locally:

Clone the repository.

Create and activate a virtual environment.

Install dependencies: pip install -r requirements.txt

Run migrations: python manage.py migrate

Start the development server: python manage.py runserver

Open your browser and go to http://127.0.0.1:8000/ to access the home page.

# Software Demo Video


# Web Pages
The application consists of several dynamically generated pages:

Home Page (/): Displays a list of all available courses. Each course links to its detail page. This page is rendered using a template that loops through a context variable containing all Course objects.

Course Detail Page (/courses/<id>/): Shows detailed information about a specific course, including its title, description, instructor, and a list of lessons. If the user is authenticated, it also displays a progress bar indicating the percentage of lessons completed (based on enrollments). A form allows the user to enroll in the course. The page dynamically fetches the course, its lessons, and the user's enrollment status from the database.

Lesson Detail Page (/courses/lesson/<id>/): (Assuming this exists) Presents the content of a specific lesson. It would typically include the lesson title, body, and possibly navigation to next/previous lessons. This page is also populated dynamically using the lesson ID from the URL.

Login/Registration Pages: Standard Django authentication pages that allow users to create an account and log in. These are built using Django's built-in authentication views with custom templates.

Each page extends a base template (base.html) that contains common navigation links (e.g., Home, Login/Logout). The navigation bar updates dynamically based on the user's authentication state.

# Development Environment

The project was developed using the following tools:

Visual Studio Code – code editor with integrated terminal and debugging.

Git – version control.

SQLite – lightweight database for development.

Django’s built-in development server – for testing locally.

The application is written in Python 3.12 using the Django 6.0 web framework. Key libraries and Django features used include:

django.contrib.auth – for user authentication and session management.

django.db.models – for defining database models (Course, Lesson, Enrollment) and relationships.

django.views.generic – for class-based views (optional, but used for simplicity in some parts).

django.template – for rendering dynamic HTML pages with template tags and filters.

django.urls – for URL routing and reverse resolution.

No external CSS frameworks were used; styling is minimal inline CSS for demonstration purposes.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* Django Documentation https://docs.djangoproject.com/en/6.0/
* MDN Web Docs: Django https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django

# Future Work

While the core functionality is in place, several enhancements would improve the application:

Implement a proper user profile system so students can see their enrolled courses and progress in one place.

Add lesson completion tracking so the progress bar reflects actual lesson views.

Improve the UI with a modern CSS framework (e.g., Bootstrap) for better responsiveness and appearance.

Add instructor roles so course creators can manage their own courses.

Include search and filtering capabilities on the course list page.

Write unit tests to ensure reliability and prevent regressions.

Deploy the application to a cloud platform (e.g., PythonAnywhere, Heroku) for public access.
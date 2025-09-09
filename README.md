# Student-feedback-system-using-Django



# Student Feedback System

This project is a web-based application for managing student feedback. It is built using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.x.
- You have installed Django (version 3.x or higher).

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/student-feedback-system.git
   cd student-feedback-system
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Django Project:**

   If you haven't already created a Django project, you can do so by running:

   ```bash
   django-admin startproject feedback
   cd feedback
   django-admin startapp student
   ```

## Project Structure

The project's directory structure should look like this:

```
student-feedback-system/
├── feedback/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── student/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── student/
│   │   │   ├── base_generic.html
│   │   │   ├── feedback_form.html
│   │   │   ├── feedback_list.html
│   │   │   ├── feedback_detail.html
│   ├── static/
│   │   ├── css/
│   │   │   ├── styles.css
│   │   ├── js/
│   │       ├── scripts.js
├── manage.py
├── requirements.txt
```

## Database Setup

1. **Run Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

3. **Load Initial Data:**

   If you have initial data to load, you can do so by creating fixtures and using:

   ```bash
   python manage.py loaddata initial_data.json
   ```

## Running the Application

1. **Start the Development Server:**

   ```bash
   python manage.py runserver
   ```

2. **Access the Application:**

   Open your web browser and go to `http://127.0.0.1:8000/` to see the application running.

## Usage

1. **Home Page:**

   - The home page lists all feedback submissions.
   - Users can click on a feedback entry to see its details.

2. **Submit Feedback:**

   - Navigate to the feedback submission form.
   - Fill out the form with required details (e.g., student name, USN, email, feedback message).
   - Submit the form to record the feedback.

3. **Feedback Details:**

   - The feedback detail page shows the submitted feedback.
   - Users can view all details of the feedback.

4. **Admin Interface:**

   - Admins can log in to the admin interface to manage feedback entries.
   - Access the admin interface at `http://127.0.0.1:8000/admin/`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


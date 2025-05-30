# Django Crud
## Simple Task Manager with Django and Bootstrap 5

This is a simple web application built with Django and styled with Bootstrap 5. It allows users to manage their tasks by creating, editing, completing, and deleting them. It also features user registration and login, and an admin panel for managing the underlying data.

## Features

* **User Authentication:**
    * User registration.
    * User login.
    * Logout functionality.
* **Task Management:**
    * Create new tasks.
    * Edit existing tasks.
    * Mark tasks as completed.
    * Delete tasks.
* **Task Views:**
    * View all pending tasks.
    * View all completed tasks.
* **Admin Panel:**
    * Django's built-in admin interface for managing users and tasks.

## Technologies Used

* [Django](https://www.djangoproject.com/): A high-level Python web framework.
* [Bootstrap 5](https://getbootstrap.com/): A powerful CSS framework for responsive design.

## Getting Started

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/LudwingArandiaa/django-crud
    cd django-crud
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    # .venv\Scripts\activate   # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Make migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an admin user.

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7.  **Open your browser and navigate to `http://127.0.0.1:8000/`** to access the application.

---

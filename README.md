# BloggingApp

BloggingApp is a Django-based web application that allows users to create, manage, and share blog posts. It features a subscription system enabling readers to subscribe to their favorite authors and receive email notifications for new posts.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

BloggingApp is designed to provide a seamless blogging experience with user-friendly interfaces and efficient content management. Built with Django, it leverages the framework's robustness to deliver a secure and scalable platform for bloggers and readers alike.

## Features

- **User Authentication**: Secure user registration and login functionality.
- **Blog Management**: Create, edit, and delete blog posts with rich text formatting.
- **Subscription System**: Readers can subscribe to authors and receive email notifications for new posts.
- **Responsive Design**: Optimized for various devices to ensure a consistent user experience.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Muzzamil-codes/BloggingApp.git
   cd BloggingApp
   ```

2. **Set up a virtual environment (recommended)**:

    ```bash
    Copy code
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    Copy code
    pip install -r requirements.txt
    ```

4. **Configure environment variables**:

    Create a .env file in the project root and add the following variables:

    ```env
    Copy code
    SECRET_KEY=your_secret_key
    EMAIL_HOST_USER=your_email@example.com
    EMAIL_HOST_PASSWORD=your_email_password
    ```
    Replace your_secret_key, your_email@example.com, and your_email_password with your actual credentials.

5. **Apply database migrations**:

    ```bash
    Copy code
    python manage.py migrate
    ```

6. **Create a superuser (for admin access)**:

    ```bash
    Copy code
    python manage.py createsuperuser
    ```

7. **Collect static files**:

    ```bash
    Copy code
    python manage.py collectstatic
    ```

## Usage

1. **Run the development server**:

    ```bash
    Copy code
    python manage.py runserver
    ```

2. **Access the application**:

    Open your web browser and navigate to http://127.0.0.1:8000/.

3. **Admin Panel**:

    Access the Django admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials created earlier.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.


For any inquiries or support, please contact Muzzamil-codes.



# Django Job Board

## Overview

The Django Job Board is a comprehensive web application built with Django that provides a platform for job postings and applications. It features a robust backend with user authentication, job management, and application tracking capabilities.

## Key Features

### Job Management

- Create and manage job listings
- Job details include:
  - Title and description
  - Salary and experience requirements
  - Job type (Full Time/Part Time)
  - Category classification
  - Image upload for job postings

### User System

- User registration and authentication
- Profile management with:
  - Contact information
  - City selection
  - Profile image upload

### Application System

- Job application functionality
- Application details include:
  - Applicant information
  - CV/Resume upload
  - Cover letter submission
  - Application tracking

### Additional Features

- Contact form for inquiries
- Admin interface for system management
- Search and filter functionality for jobs

## Technology Stack

- **Framework**: Django 3.2
- **Database**: SQLite (default)
- **Authentication**: Django Auth System
- **File Handling**: Django FileField/ImageField
- **Frontend**: HTML, CSS, JavaScript

## Installation

### Prerequisites

- Python 3.8+
- pip package manager

### Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/AhmedMohammedSalah/Django-job-board.git
   cd Django-job-board
   ```

2. Create and activate virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create superuser (optional):

   ```bash
   python manage.py createsuperuser
   ```

6. Start development server:
   ```bash
   python manage.py runserver
   ```

## Usage

### Accessing the Application

- Web interface: `http://127.0.0.1:8000/`
- Admin interface: `http://127.0.0.1:8000/admin/`

### Key Endpoints

- Job Listings: `/jobs/`
- Job Details: `/jobs/<slug>/`
- User Profile: `/accounts/profile/`
- Contact Form: `/contact-us/`

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a new branch for your feature
3. Submit a pull request with detailed description

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

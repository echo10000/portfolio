# Jericho Blando — Personal Portfolio Website

A personal portfolio website built with **Django**, deployed on **PythonAnywhere**.

🌐 **Live Site:** https://jericho_blando.pythonanywhere.com  
📁 **GitHub:** https://github.com/jericho-blando/portfolio

---

## 📋 Project Overview

This portfolio showcases:
- Personal introduction and profile photo
- About page with background and career goals
- Skills section with proficiency bars
- Projects section (minimum 3 projects)
- Education timeline
- Contact form that saves messages to the database

**Course:** ITS 305 — Section A  
**Midterm Project:** Personal Portfolio Website using Django

---

## 🛠 Tech Stack

| Layer        | Technology              |
|--------------|-------------------------|
| Backend      | Python 3.x, Django 4.2  |
| Frontend     | HTML5, CSS3, JavaScript |
| Database     | SQLite (dev) / MySQL (prod) |
| Hosting      | PythonAnywhere          |
| Version Control | Git & GitHub         |

---

## 📁 Project Structure

```
portfolio_project/
├── manage.py
├── requirements.txt
├── README.md
├── portfolio_site/          # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── portfolio/               # Django app
    ├── __init__.py
    ├── admin.py             # Admin panel config
    ├── models.py            # Database models
    ├── views.py             # Page views
    ├── urls.py              # URL routing
    ├── migrations/          # Database migrations
    ├── templates/portfolio/ # HTML templates
    │   ├── base.html
    │   ├── home.html
    │   ├── about.html
    │   ├── skills.html
    │   ├── projects.html
    │   ├── education.html
    │   └── contact.html
    └── static/portfolio/
        ├── css/style.css
        └── js/main.js
```

---

## ⚙️ Local Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/jericho-blando/portfolio.git
cd portfolio
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations (creates DB + seeds sample data)
```bash
python manage.py migrate
```

### 5. Create a superuser (for Django admin)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

---

## 🔧 Django Admin Panel

Go to http://127.0.0.1:8000/admin/ and log in with your superuser credentials.

From the admin panel you can:
- **Edit your Profile** — name, tagline, bio, photo, social links
- **Add/Edit Skills** — set category and proficiency percentage
- **Add/Edit Projects** — title, description, tech stack, GitHub link
- **Add/Edit Education** — school, degree, years attended
- **View Contact Messages** — messages submitted through the contact form

---

## 🚀 Deployment on PythonAnywhere

### 1. Upload your code
```bash
# On PythonAnywhere bash console:
git clone https://github.com/jericho-blando/portfolio.git
```

### 2. Create a virtual environment
```bash
mkvirtualenv --python=python3.10 portfolio-env
pip install -r requirements.txt
```

### 3. Configure the Web App
- Go to **Web** tab → **Add a new web app**
- Choose **Manual configuration** → **Python 3.10**
- Set **Source code:** `/home/jericho_blando/portfolio`
- Set **Working directory:** `/home/jericho_blando/portfolio`
- Set **Virtualenv:** `/home/jericho_blando/.virtualenvs/portfolio-env`

### 4. Edit WSGI file
In the Web tab, click the WSGI file link and replace its content with:
```python
import os
import sys

path = '/home/jericho_blando/portfolio'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_site.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 5. Configure static files
In the Web tab → **Static files**:
| URL          | Directory                                          |
|--------------|----------------------------------------------------|
| /static/     | /home/jericho_blando/portfolio/staticfiles/        |
| /media/      | /home/jericho_blando/portfolio/media/              |

Then run:
```bash
python manage.py collectstatic
```

### 6. Update settings.py for production
```python
ALLOWED_HOSTS = ['jericho_blando.pythonanywhere.com']
DEBUG = False
```

### 7. Migrate and reload
```bash
python manage.py migrate
```
Click **Reload** in the Web tab.

---

## 📌 Notes

- Replace all placeholder content (email, GitHub links, school name) in the Django admin
- Upload your profile photo via the admin panel under **Profile**
- The contact form saves messages to the database — check them in the admin panel

---

## 👤 Author

**Jericho Blando**  
BS Information Technology — ITS 305, Section A

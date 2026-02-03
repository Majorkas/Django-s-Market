# Django Marketplace

A full-featured online marketplace built with Django 4.2, featuring user authentication, item listings, image uploads, and a modern Tailwind CSS interface.

## 🚀 Features

- **User Authentication**: Secure signup, login, and profile management
- **Marketplace**: Browse, create, edit, and delete item listings
- **Image Management**: Upload and store images via Cloudinary
- **Responsive Design**: Modern UI built with Tailwind CSS and shadcn components
- **User Profiles**: Manage personal information and view your listings
- **Search & Filter**: Find items in the marketplace
- **Admin Dashboard**: Manage users and listings through Django admin

## 📋 Prerequisites

- Python 3.13+
- uv package manager (recommended) or pip
- PostgreSQL (for production)
- Cloudinary account (for image storage)

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd ucd-pa-frameworks-assessment/djangos_marketplace
```

### 2. Create and activate virtual environment

```bash
# Create venv with uv
uv venv

# Activate on Windows
.venv\Scripts\activate

# Activate on Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the `djangos_marketplace` directory:

```env
SECRET_KEY_DJANGO=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Cloudinary Configuration
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# Email Configuration (for allauth)
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Database (for production)
DATABASE_URL=postgresql://user:password@localhost/dbname

# Render.com (for deployment)
RENDER_EXTERNAL_HOSTNAME=your-app.onrender.com
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

### 7. Collect static files

```bash
python manage.py collectstatic
```

### 8. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## 📦 Dependencies

### Core Framework

- **[Django 4.2.27](https://docs.djangoproject.com/en/4.2/)** - High-level Python web framework
  - Provides the core functionality for the web application
  - Includes ORM, admin interface, authentication, and URL routing

### Authentication

- **[django-allauth 0.63.3](https://docs.allauth.org/)** - Integrated authentication solution
  - Handles user registration, login, logout, and email verification
  - Supports social authentication (optional)
  - Password reset functionality

### Forms & UI

- **[django-crispy-forms 2.1](https://django-crispy-forms.readthedocs.io/)** - Advanced form rendering
  - Controls form rendering behavior
  - Provides template packs for different CSS frameworks
  
- **[crispy-tailwind 1.0.3](https://github.com/django-crispy-forms/crispy-tailwind)** - Tailwind CSS template pack
  - Renders Django forms with Tailwind CSS classes
  - Provides proper styling for form fields, labels, and errors

- **[django-cotton 1.0.13](https://django-cotton.com/)** - Component-based templating
  - Allows creation of reusable UI components
  - Used for shadcn-style components (cards, buttons, alerts, etc.)
  - Simplifies template organization

- **[Tailwind CSS](https://tailwindcss.com/)** - Utility-first CSS framework
  - Provides low-level utility classes for building custom designs
  - Responsive design utilities
  - Dark mode support
  - Used throughout the project for styling via CDN

### Image Management

- **[cloudinary 1.41.0](https://cloudinary.com/documentation/django_integration)** - Cloud-based image management
  - Image upload and storage
  - Image transformation and optimization
  - CDN delivery for fast loading

- **[django-cloudinary-storage 0.3.0](https://github.com/klis87/django-cloudinary-storage)** - Django storage backend
  - Integrates Cloudinary with Django's storage system
  - Works seamlessly with ImageField and FileField

- **[Pillow 10.3.0](https://pillow.readthedocs.io/)** - Python Imaging Library
  - Required for Django's ImageField
  - Image processing and validation

### Configuration & Environment

- **[python-dotenv 1.0.0](https://saurabh-kumar.com/python-dotenv/)** - Environment variable management
  - Loads environment variables from `.env` file
  - Keeps sensitive data out of source code

### Production & Deployment

- **[gunicorn 21.2.0](https://docs.gunicorn.org/)** - Python WSGI HTTP Server
  - Production-grade web server
  - Required for deployment on platforms like Render.com

- **[psycopg2-binary 2.9.9](https://www.psycopg.org/docs/)** - PostgreSQL adapter
  - Connects Django to PostgreSQL databases
  - Required for production deployments

- **[dj-database-url 2.1.0](https://github.com/jazzband/dj-database-url)** - Database configuration
  - Parses database URLs from environment variables
  - Simplifies database configuration in production

- **[whitenoise 6.6.0](https://whitenoise.readthedocs.io/)** - Static file serving
  - Serves static files in production
  - Compression and caching for better performance

## 🎨 Styling with Tailwind CSS

This project uses **[Tailwind CSS](https://tailwindcss.com/)**, a utility-first CSS framework that provides low-level utility classes to build custom designs.

### Key Concepts

**Utility-First**: Instead of writing custom CSS, you compose designs using pre-defined utility classes:

```html
<!-- Traditional CSS -->
<div class="card">...</div>
<style>.card { padding: 1rem; background: white; border-radius: 0.5rem; }</style>

<!-- Tailwind CSS -->
<div class="p-4 bg-white rounded-lg">...</div>
```

**Responsive Design**: Built-in responsive modifiers:

```html
<div class="w-full md:w-1/2 lg:w-1/3">
  <!-- Full width on mobile, half on tablet, third on desktop -->
</div>
```

**Component Classes**: This project uses custom component classes via django-cotton:

```html
<c-card>
  <c-card.header>
    <c-card.title>Title</c-card.title>
  </c-card.header>
  <c-card.content>Content here</c-card.content>
</c-card>
```

### Tailwind Resources

- **[Official Documentation](https://tailwindcss.com/docs)** - Complete guide and API reference
- **[Tailwind UI](https://tailwindui.com/)** - Official component library (some paid)
- **[Tailwind Play](https://play.tailwindcss.com/)** - Online playground
- **[shadcn/ui](https://ui.shadcn.com/)** - Component library (inspiration for this project)

### Common Tailwind Patterns in This Project

```html
<!-- Container with padding -->
<div class="container mx-auto px-4 py-8">

<!-- Card layout -->
<div class="rounded-lg border bg-card text-card-foreground shadow-sm">

<!-- Button styling -->
<button class="inline-flex items-center justify-center rounded-md bg-primary px-4 py-2 text-primary-foreground">

<!-- Grid layout -->
<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">

<!-- Flexbox utilities -->
<div class="flex items-center justify-between">
```

## 🗂️ Project Structure

```
djangos_marketplace/
├── djangos_marketplace/          # Project configuration
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Main URL configuration
│   └── wsgi.py                  # WSGI configuration
├── marketplace/                  # Marketplace app
│   ├── models.py                # MarketItem model
│   ├── views.py                 # Marketplace views
│   ├── urls.py                  # Marketplace URLs
│   └── admin.py                 # Admin configuration
├── users/                        # Users app
│   ├── models.py                # UserProfile model
│   ├── views.py                 # Profile views
│   ├── forms.py                 # Profile forms
│   ├── signals.py               # Auto-create profiles
│   └── urls.py                  # User URLs
├── templates/                    # HTML templates
│   ├── base.html                # Base template
│   ├── account/                 # Authentication templates
│   ├── marketplace/             # Marketplace templates
│   ├── users/                   # User templates
│   └── cotton/                  # Reusable components
├── staticfiles/                  # Collected static files
├── media/                        # User uploaded files (local dev)
├── requirements.txt             # Python dependencies
├── manage.py                    # Django management script
└── .env                         # Environment variables (not in git)
```

## 🚢 Deployment to Render.com

### 1. Create a Render account

Sign up at [render.com](https://render.com)

### 2. Create a PostgreSQL database

- Go to **Dashboard** → **New** → **PostgreSQL**
- Note the **Internal Database URL**

### 3. Create a web service

- Go to **Dashboard** → **New** → **Web Service**
- Connect your GitHub repository
- Configure:
  - **Name**: your-app-name
  - **Environment**: Python 3
  - **Build Command**: `./build.sh`
  - **Start Command**: `gunicorn djangos_marketplace.wsgi:application`

### 4. Set environment variables

Add these in the Render dashboard:

```
SECRET_KEY_DJANGO=<generate-a-new-secret-key>
DEBUG=False
ALLOWED_HOSTS=.onrender.com
DATABASE_URL=<your-postgres-url>
CLOUDINARY_CLOUD_NAME=<your-cloud-name>
CLOUDINARY_API_KEY=<your-api-key>
CLOUDINARY_API_SECRET=<your-api-secret>
EMAIL_HOST_USER=<your-email>
EMAIL_HOST_PASSWORD=<your-password>
PYTHON_VERSION=3.13.5
```

### 5. Deploy

Render will automatically deploy your application. Monitor the logs for any errors.

## 📝 Usage

### Creating a Listing

1. Sign up or log in
2. Click **Post Item** in the navigation
3. Fill in the item details:
   - Title
   - Description
   - Price
   - Contact information
   - Upload an image
4. Click **Post Item**

### Managing Listings

- View all your listings in your **Profile**
- Edit or delete items from your profile
- Mark items as available/unavailable

### Browsing the Marketplace

- Visit the **Market** page to see all available items
- Click on an item to see full details
- Contact sellers via the contact information provided

### Accessing Admin Panel

Visit `http://127.0.0.1:8000/admin` and log in with your superuser credentials.




## 🙏 Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Django_shadcn](https://shadcn-django.com/) - Component design 
- [Cloudinary](https://cloudinary.com/) - Image management
- [Render.com](https://render.com/) - Hosting platform

Project Link: [https://github.com/yourusername/django-marketplace](https://github.com/yourusername/django-marketplace)

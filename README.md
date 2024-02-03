
---

### Project Overview:

A project to intaract with csv file using django restframework

### What I Did:

  
### How I Made It Happen:

- **Technology Used:** I used Django and Django REST Framework.
  
- **Testing and Notes:**
   - Checked everything was working using a tool called Postman.
   - Wrote down all the steps in a document so others can understand and use it later.

### What I Learned:

I found out a lot about how to make systems work better. I also learned new ways to secure systems and how to check if they're working well.







Installation process 



---

## Project Structure

The project is structured as follows:

- `backend/` - Django project folder
- `product/` - Django app for vendor management
- `foxiomvenv/` - Virtual environment for Python

## Setup Instructions

### 1. Create Virtual Environment

```
    py -m venv venv
```

### 2. Activate Virtual Environment

```
    venv\scripts\activate
```

### 3. Install Dependencies

Install required packages using pip:

```
    pip install django djangorestframework django-cors-headers
```

### 4. Create Django Project and App

```

    django-admin startproject backend
    django-admin startapp product
```

### 5. Configuration

#### Update `settings.py`

Add the following apps to `INSTALLED_APPS` in `backend/settings.py`:

```
    INSTALLED_APPS = [
        # ...
        'product',
        'rest_framework',
        'corsheaders',

        # ...
    ]
```

#### Configure CORS

Add the CORS middleware to `MIDDLEWARE` in `backend/settings.py`:

```
    MIDDLEWARE = [
        # ...
        'corsheaders.middleware.CorsMiddleware',
        # ...
    ]
```

### 6. URL Configuration

Connect app URLs to project URLs in `product/urls.py`:

```
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
    path('product/<str:product_id>/', ProductDetailsAPIView.as_view(), name='product-details'),
    path('top-rated/', TopRatedProductsAPIView.as_view(), name='top-rated-products'),
    path('average-discounts/', AverageDiscountByCategoryAPIView.as_view(), name='average-discounts'),
    path('products/<str:category>/', ProductsByCategoryAPIView.as_view(), name='products-by-category'),
    

]
```

### 7. Database Setup

Run Django migrations to set up the database:

```
    python manage.py makemigrations
    python manage.py migrate
```

### 8. Run Development Server

Start the development server:

```
    python manage.py runserver
```











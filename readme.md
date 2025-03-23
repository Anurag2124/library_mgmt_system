
# **Library Management API**

A Django REST API for managing books, where only **admins** can create, update, and delete books, while **students** (unauthenticated users) can only read them.

---

## **Setup Instructions**

### **1. Clone the Repository**  
```bash
git clone <repository_url>
cd <project_directory>
```

### **2. Create and Activate a Virtual Environment**  

#### **For Windows (Command Prompt)**  
```bash
python -m venv env
env\Scripts\activate
```

#### **For macOS/Linux**  
```bash
python3 -m venv env
source env/bin/activate
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Configure Environment Variables**  
Create a **`.env`** file in the root directory and add the following:  
```
DB_PASSWORD=your_database_password
```

### **5. Apply Migrations**  
```bash
python manage.py makemigrations
python manage.py migrate
```

### **6. Create a Superuser (Admin)**  
```bash
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

### **7. Run the Development Server**  
```bash
python manage.py runserver
```
The API will be available at **`http://127.0.0.1:8000/`**

---

## **Django Project Settings**

Make sure the following settings are present in `settings.py`:

### **Installed Apps**  
```python
INSTALLED_APPS = [
    'api',
    'rest_framework',
    'rest_framework_simplejwt',
]
```

### **Database Configuration (MySQL)**  
```python
import os
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library',
        'USER': 'root',
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```

### **Custom User Model**  
```python
AUTH_USER_MODEL = 'api.AdminUser'
```

### **JWT Authentication Setup**  
```python
from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),  # 1 day access token
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),  # 7 days refresh token
    "ROTATE_REFRESH_TOKENS": True,  # Refresh token updates on use
    "BLACKLIST_AFTER_ROTATION": True,  # Old refresh tokens become invalid
    "AUTH_HEADER_TYPES": ("Bearer",),  # Authorization: Bearer <token>
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}
```

---

## **Working with Endpoints**

### **1. User Authentication Endpoints**

- **Login (Admin)**  
  - **POST** `/api/token/`  
  Admin can log in with **email** and **password** to receive JWT tokens (access and refresh).  

  Example Request Body:  
  ```json
  {
      "email": "admin@example.com",
      "password": "your_password"
  }
  ```


### **2. Book Management Endpoints** (For Admin)

Admin users can **create**, **update**, and **delete** books.

- **Create Book**  
  - **POST** `/api/books/`  
  Admin can create a new book by providing book details.

  Example Request Body:  
  ```json
  {
      "title": "Book Title",
      "author": "Author Name",
      "published_date": "2023-01-01"
  }
  ```

- **List All Books**  
  - **GET** `/api/books/`  
  Anyone (including students) can view a list of all books.

- **Retrieve Book Details**  
  - **GET** `/api/books/{id}/`  
  Anyone (including students) can view details of a specific book by its ID.

- **Update Book**  
  - **PUT** `/api/books/{id}/`  
  Admin can update a book's details.

  Example Request Body:  
  ```json
  {
      "title": "Updated Book Title",
      "author": "Updated Author Name",
      "published_date": "2023-01-01"
  }
  ```

- **Delete Book**  
  - **DELETE** `/api/books/{id}/`  
  Admin can delete a specific book.

---

## **Permissions**

- **IsAdminOrReadOnly**:  
  - **Admins** (authenticated users) can **create**, **update**, and **delete** books.
  - **Students** (unauthenticated users) can only **read** books (i.e., list and retrieve books).

---

### **Final Notes**

- Ensure the `.env` file with your database password is added before running the project.
- The JWT tokens expire after 1 day, and refresh tokens are valid for 7 days.
- Admins have the ability to manage (create, update, delete) books, while students can only read book details.

---

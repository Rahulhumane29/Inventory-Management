Inventory Management API

1. A Django REST Framework-based Inventory Management system with:
2. CRUD APIs
3. Filtering support
4. PDF export
5. Excel export


Tools & Technologies

1. Python
2. Django
3. Django REST Framework
4. ReportLab (PDF generation)
5. OpenPyXL (Excel generation)
6. SQLite (default DB)

1. Create Virtual Environment
python -m venv inventory 
Activate it:
.\inventory\Scripts\activate

2. Install Dependencies
pip freeze > requirements.txt
pip install django djangorestframework reportlab openpyxl django-filter

3. Apply Migrations
python manage.py makemigrations
python manage.py migrate

4. Create Superuser
python manage.py createsuperuser

5. How to Run the Server
python manage.py runserver
Server will run at:
http://127.0.0.1:8000/

6.How to Test APIs
You can test APIs using:
1. Postman
2. Browser (for GET APIs)

7.Base URL
http://127.0.0.1:8000/api/items/

1) GET
http://127.0.0.1:8000/api/items/

2) POST
http://127.0.0.1:8000/api/items/
JSON Body:
{
    "name": "Laptop",
    "description": "Dell i7 16GB RAM",
    "quantity": 10,
    "price": 65000.00
}

3) Update Item
http://127.0.0.1:8000/api/items/<id>/

4) Delete Item
http://127.0.0.1:8000/api/items/<id>/

5) Filtering
http://127.0.0.1:8000/api/items/?min_quantity=30

8. How to Generate PDF
http://127.0.0.1:8000/api/items/export/pdf/

9. How to Generate Excel
http://127.0.0.1:8000/api/items/export/excel/



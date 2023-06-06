STEP 1: Change directory to \ecommerce, Create a virtual environment and activate it then install requirements using command:
    pip install -r requirements.txt

STEP 2: Run Followings commands for database migration:
    a) python manage.py makemigrations
    b) python manage.py migrate

STEP 3: Create superuser using following command:
    python manage.py createsuperuser --email admin@example.com --username admin

STEP 4: For run project use command in project root directory:
    python manage.py runserver


APIs

1. Creating multiple orders
Method: POST
Url: http://127.0.0.1:8000/api/orders/

Request Payload:

{
"user": <user_id>,   
"status": "PENDING",
"items": [
{"name": "Item 1", "quantity": 2, "price": 10.0},
{"name": "Item 2", "quantity": 1, "price": 15.0}
]
}

Note:  Please use order_id = 1 as we have created only one user which is admin having user_id = 1


2. Get single order by order_id
Method: GET
Url: http://127.0.0.1:8000/api/orders/<int:order_id>/

3. Get list of all orders with it's all item
Mehtod: GET
Url: http://127.0.0.1:8000/api/orders/list/

4. Update the status of Existing Order status by order_id:
Method: PUT
Url: http://127.0.0.1:8000/api/orders/<int:order_id>/status/

Request Payload:
{
    "status" : "PENDING" or "DELIVERED" or "COMPLETED"
}

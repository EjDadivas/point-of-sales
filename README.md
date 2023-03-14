# point-of-sales

This project is a Django-based web application that manages items in a point of sale system.

Changes Made:

-Inside the item app folder, the following classes were added to the models.py file: item, order, item_order.
-The templates for base.html and list_item.html were modified to display data. The data is passed from the views.py file in the item app to the templates using Django's templating language
-In the project urls.py file, URLs path for the item app were included.
-The views.py file in the item app was modified with the following functions: item_view, list_item, add_item, delete_item, update_item.
-Registered the models in admin.py of item app.

New Files:

-migrations folder for the models.py.
-The item app urls.py file was created with the following paths: '', 'list_item', 'add_item', 'delete_item/int:pk', and 'update_item/int:pk'.
-A requirements.txt file was included to install the necessary dependencies.
-A posdb_dump.sql file was included with sample data for item, order, and item_order.
-Please use the requirements.txt file to install the required dependencies, and the posdb_dump.sql file to populate the database with sample data.

Thank you for using this Django-based point of sale system.

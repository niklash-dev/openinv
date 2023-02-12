# OpenInv - Inventory Management System

A Django based web service that allows users to build an inventory.

## Features
- User authentication and authorization
- Inventory item management (create, read, update, delete)
- Search and filter inventory items
- Generate reports on inventory status
## Prerequisites
- Python 3.x
- Django 3.x
- Virtual environment (optional but recommended)
## Installation
1. Clone the repository: git clone https://github.com/<your-username>/inventory-management-system.git
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
3. Install the required packages: 
    ```bash
    pip install -r requirements.txt
    ```
4. Run migrations:
    ```bash
    python manage.py migrate
    ```
5. Start the development server:
    ```bash
    python manage.py runserver
    ```
## Usage
Open a web browser and go to http://localhost:8000/. Create a user account (http://localhost:8000/admin) or log in if you already have one. Start managing your inventory items!
## Contributions
This project is open for contributions. If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Submit a pull request
6. License


This project is licensed under the GNU GPLv3 License. See LICENSE for details.
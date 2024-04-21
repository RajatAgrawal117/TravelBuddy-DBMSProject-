# Travel Website Project

This is a Django project for a travel website that uses Bootstrap for the frontend and MySQL for the database. The website allows users to select a destination and view available activities and accommodations for that destination.

## Features

- User-friendly interface with Bootstrap styling
- Destination selection dropdown
- Display of available activities and accommodations based on the selected destination
- Django backend with models for destinations, activities, and accommodations
- MySQL database for storing and fetching data

## Installation

1. Clone the repository: `git clone https://github.com/your-username/travel-website.git`
2. Navigate to the project directory: `cd travel-website`
3. Create and activate a virtual environment (optional but recommended)
4. Install the required Python packages: `pip install -r requirements.txt`
5. Set up the MySQL database and update the database configuration in `settings.py`
6. Run database migrations: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`

## Usage

1. Open your web browser and go to `http://localhost:8000`
2. Select a destination from the dropdown menu on the home page
3. Click the "Submit" button
4. The available activities and accommodations for the selected destination will be displayed

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework used
- [Bootstrap](https://getbootstrap.com/) - The CSS framework used for styling
- [MySQL](https://www.mysql.com/) - The database management system used

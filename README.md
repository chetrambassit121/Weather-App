<h3>Weather Web Application</h3>
- User can input weather condition and receive a list of US based cities experiencing that condition<br>
- User can add/find/delete a city based on its name<br>
- User can upload xlsx files into the database<br><br>

Technologies used for this Application:
- Python (Language) https://www.python.org/downloads/
- Django WEB Framework (Python Framework) https://docs.djangoproject.com/en/4.1/
- Docker (Container) https://github.com/docker/awesome-compose/tree/master/official-documentation-samples/django/
- Docker Desktop App https://docs.docker.com/get-docker/
- Visual Studio Code (VSC) (Text-Editor) https://code.visualstudio.com/Download (optional)

API's Required:
- Open Weather API https://openweathermap.org/api
- Sign up to get your own API Key

INITIAL SETUP:
- Download or clone this project into a folder directory on your local machine. (Visual Studio Code use Git Clone extension).
- Access your terminal, navigate to the folder directory.
- Create virtual environment  ...  COMMAND: python -m venv venv
- Activate virtual environment ... COMMAND: venv/Scripts/activate 
- Change directory to WeatherApp ... COMMAND: cd WeatherApp/

Starting project WITH DOCKER: (MUST HAVE DOCKER DOWNLOADED)               
- Do Initial Setup first
- COMMAND: docker-compose up
- Access localhost:3000 in web browser
- Additional commands in Docker.txt

Starting project WITHOUT DOCKER:
- Do Initial Setup first
- COMMAND: pip install requirements.txt
- COMMAND: python manage.py migrate
- COMMAND: python manage.py runserver
- Access localhost:8000 in web browser
- Additional commands in DjangoPython.txt

Uploading xlsx files to database:
- After initial setup and starting project
- go to upload url
- Insert the USCities.xlsx and upload
- Data from xlsx file will be stored into djangos database

<h3>Weather Web Application</h3>
- User can input weather condition and receive a list of US based cities experiencing that condition
- User can add/find/delete a city based on its name
- User can upload xlsx files into the database

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
- Create virtual enviorment  ...  COMMAND: python -m venv venv
- Activate virtual enviorment ... COMMAND: venv/Scripts/activate 
- Change directory to WeatherApp ... COMMAND: cd WeatherApp/

Starting project WITH DOCKER: (MUST HAVE DOCKER DOWNLOADED)
- COMMAND: docker-compose up
- Access localhost:3000 in web browser

Starting project WITHOUT DOCKER:
- COMMAND: pip install requirements.txt
- COMMAND: python manage.py migrate
- COMMAND: python manage.py runserver
- Access localhost:8000 in web browser

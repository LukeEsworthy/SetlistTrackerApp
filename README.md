# SetlistTrackerApp
An app designed by Luke Esworthy and built with Django and SQL

## Purpose:
My idea behind Setlist Tracker was simple: help people track the popularity of songs they play. While that's an oversimplified explanation, the app really is that simple.
The primary target for this app is officially licensed DJs, as using this app will help them note which songs are popular and which songs aren't. They can use this data when creating a setlist for future events. 
Maybe a song was popular at a club but a hard miss at a wedding. Using data collected with this app, they can narrow down what at type of events to play each song, thus increasing their effectiveness of having hit setlists,
and hopefully advancing their popularity and success.

The secondary target for my app is, basically, everyone. The official roadtrip DJ, the backyard BBQ DJ. My friends and I never took lightly the duty of Designated DJ, and when handed the aux cord,
the pressure was on. Having different friend groups with their own musical preferences and moods makes it difficult to create one playlist, and being able to track what songs to play with what friend group
would have saved me from having my DJ duties revoked for a car ride more than once!

## Start using Setlist Tracker:
* Clone down the repo and ```cd``` into it
* Create and activate your virtual environment for this project:
  * ```python -m venv setlistenv```
  * ```source ./setlistenv/bin/activate```
* Install the dependencies:
  * ```pip install -r requirements.txt```
* Create a database from models:
  * ```python manage.py makemigrations setlisttrackerapp```
  * ```python manage.py migrate```
* Create a superuser for your local version of the app:
  * ```python manage.py createsuperuser```
* Run your server and start using the app!
  * ```python manage.py runserver```

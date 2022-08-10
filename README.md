# About GlobalCovidCases
Main purpose is to display the number of deaths, confirmed, newly confirmed and global vaccination status. This site has really helped me expand my knowledge on how to gather and manipulate data for my own personal use, I managed to link folium
a package for Python to display the number of covid cases on a Leaflet map with extreme accuracy while at the same time using a csv to display the red dots. The website fully updates in realtime and displays all current data regarding the virus.

[![Link - Global Covid Cases](https://img.shields.io/badge/Link-Global_Covid_Cases-3693F3?style=for-the-badge&logo=<svg+role%3D"img"+viewBox%3D"0+0+24+24"+xmlns%3D"http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg"><title>iCloud<%2Ftitle><path+d%3D"M13.762+4.29a6.51+6.51+0+0+0-5.669+3.332+3.571+3.571+0+0+0-1.558-.36+3.571+3.571+0+0+0-3.516+3A4.918+4.918+0+0+0+0+14.796a4.918+4.918+0+0+0+4.92+4.914+4.93+4.93+0+0+0+.617-.045h14.42c2.305-.272+4.041-2.258+4.043-4.589v-.009a4.594+4.594+0+0+0-3.727-4.508+6.51+6.51+0+0+0-6.511-6.27z"%2F><%2Fsvg>)](https://www.globalcovidcases.com)
# Technology Used :hammer_and_wrench:

Frontend :gear:| Description|
-------|------------|
CSS    | Everything within the pages were styled using CSS, the design again is very minimilistic but clean and easy to use. Also, used it as a way to make it responsive to phones and other devices. 
Bootstrap| Visual aspects such as the textfield and button elements.
HTML   | Stores the Home/About pages, also used it to template tag all the necessary elements such as displaying the weather conditions which I defined via the Django application.

Backend :toolbox:| Description|
-------|------------|
Django | Django is a well known Python backend web framework which I used to gather all the necessary information. Mainly used for template tagging and connecting all the HTML pages as well as migrating my project to a database. Also used as a form of site/token protection from malicious intruders.
Python | All the script was written in Python alongside Django for backend implementation primarily functions regarding the logic for how the red dots are placed onto the Leaflet map while at the same time using Python to grab an API to display up to date numbers ([https://covidtracking.com/data/api](https://covid19api.com/)).
[Covid19Api](https://covid19api.com/) | Used to display up to date realtime covid confirmations as shown on the home screen of my website.

Libraries :books:| Description|
-------|------------|
requests  | Used to fetch URLs for Python, uses the requests function to grab any website information using a variety of different protocols. In my case I used it to fetch an API and collected specific information from within the API.
whitenoise| Due to the fact Django does not have a way of supporting static files into production, whitenoise clears this barrier by placing all the required information into it's own separate folder which the web host (Heroku) can read from and apply any new changes.
gunicorn| [Gunicorn](https://github.com/benoitc/gunicorn) known as 'Green Unicorn' is a Python specific web server gateway. I used it as a way to pass requests data to my web application all through Heroku.
folium | Used to display the Leaflet map shown on the website, mainly used to display and render highly detailed maps. Includes a marker to point to the specific location that the user has searched for via the search field.
geocoder | Gathered realtime world coordinates which then are converted to georaphic information using longitude and latitude inputs. Maintains the precise location of of real world coordinates alongside folium, procedurally generates a single point instance of where a location is.

Web-services :spider_web:| Description|
-------|------------|
Heroku | Heroku is a cloud platform for hosting and maintaining website information which I used to later connect the platform with GoDaddy. 
GoDaddy| Domain was registered from GoDaddy alongside all DNS setup.

Personal Website that is underdevelopement.
Back-end uses Python and Django franework. Front-end uses Bootstrap for CSS and Javascript for Html improvement.

python manage.py runserver
* hosts webserver at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Current working urls can be found in the homeapp/urls.py:
* home
* home/register
* about

'home/register' -> creates an Account in the SQLite DB with the parameters: username, email, password
* for testing purposes, 'home/test' demonstrates an admins pov for user accounts, which gives admins power to create and delete any user

Other working url:
* admnin/
  * access to all databases
  * only django superuser can access

Goals of this project(urls):
* Library/
  * /set/ -> display from database, add/delete from db, move terms/cells order, filter
  * css for library & set pages
* Home/
  * Login/Register -> create a user acc to have access to site
  * Home page css

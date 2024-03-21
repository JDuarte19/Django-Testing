Personal Website that is underdevelopement.

python manage.py runserver
* hosts webserver at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Current working urls can be found in the homeapp/urls.py:
* homeapp/library
* homeapp/library/set/int pk
  * int pk is set for the primary key of the current database being requested
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

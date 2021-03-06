# Zoo
A basic CRUD demo featuring an API for animals at a zoo. SQLite DB, Django 2.1.3.

## About this code
I've tested the endpoints with Django test cases as best as I can think to do. In the `zoo/zoo/` path,
`./manage.py runserver` seems to work fine, and I registered the models with the admin site. There isn't yet any initial data except for that used in the tests. There are 10 tests, which can be run with a simple `./manage.py test`. Of course, tracking the SQLite DB file in Git was a mistake! Luckily this isn't anything sensitive.

Note: There was no index page specified in the document, so the following URL paths are all accessible from the `animals/` app root:

* `animals/population/`: Count of animals in the zoo.
* `GET animals/animal/Tetley/`: Retrieve data for the example animal named Tetley.
* `POST animals/animal/`: Attempt to create a new animal.
* `animals/hungry/`: Responds with a plain count of the number of animals who haven't eaten in the past 2 days (`last_feed_time`).
* `animals/feed/`: On POST, attempts to 'feed' the animal with a given name in the request data.

## What I'd rather have done
Django Rest Framework with URL routing and ViewSets is something I'm quite fond of these days, for pure API work.

## Django version
I avoided a CVE alert on Github by bumping the Django version to 2.1.3, which didn't seem to have any noticeable effect on the nature of the assessment as far as I can tell.


### Thanks, Marc.

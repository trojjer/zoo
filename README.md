# Zoo
A basic CRUD demo featuring an API for animals at a zoo.

## About this code
I've tested the endpoints with Django test cases as best as I can think to do.
`./zoo/zoo/manage.py runserver` seems to work fine, and I registered the models with the admin site. Note: There was no index page specified in the document, so the URLs are all accessible from the `animals/` app root.

## What I'd rather have done
Django Rest Framework with URL routing and ViewSets are something I'm quite fond of these days, for pure API work.

## Django version
I avoided a CVE alert on Github by bumping the Django version to 2.1.3, which didn't seem to have any noticeable effect on the nature of the assessment as far as I can tell.


### Thanks, Marc.

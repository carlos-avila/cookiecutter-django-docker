# {{cookiecutter.project_name}}

By *{{cookiecutter.project_author}}*

This README would normally document whatever steps are necessary to get your application up and running.

### A short description of {{cookiecutter.project_name}}.

# Requirements
* virtualenv
* npm
* fswatch
* unison

##Basic Commands

###Setting Up Your Users


* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Test coverage ###

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

### Running tests with py.test ###



    $ py.test

Deployment
----------
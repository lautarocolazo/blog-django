# Overview

This is a full-stack blog website with user authentication built with Django, Django templates, and tailwind css. I know that many people mainly use Django to develop back-end and then they use a different front-end framework like React but I wanted to learn the full-stack experience with Django itself.

# App overview

As mentioned above, this is a full-stack blog website with authentication. It handleds users sign up and login, and it handleds specifics views if you are and admin user a.k.a superuser in Django.
As an admin user you will be able to create new blog posts, edit any existing blog posts, and delete them.
As a logged in user, independently of your role, you will be able to post comments in each blog post, and delete them if desired.

# To run the app execute the following steps:

My app has a `requirements.txt` file, so , if you don't want to install the dependencies locally, you can create a virtual environment first.
I am a linux user, and there are many different tools that you can use to accomplish the exact same thing, so I will indicate what works for me with the tool that I use. The steps will work for Ubuntu based distros.
If you are running a different OS, Google how to create a virtual environment in such OS.

## Previous requirements:

You will need python 3+ and pip installed in your system

## Clone the repo

```bash
git clone git@github.com:lautarocolazo/blog-django.git
```

## Install virtualenv if you don't have it

```bash
pip install virtualenv
```

Or

```bash
pip3 install virtualenv
```

## Create virtual environment called venv

```bash
virtualenv --python python3 venv
```

## Activate virtual environment

```bash
source venv/bin/activate
```

## Database

For security reasons I am not pushing any db to the respository. For that reason, you will have to run the following command lines so Django can create the sqlite3 database.

First:

```bash
python3 manage.py makemigrations
```

and then:

```bash
python3 manage.py migrate
```

Or:

```bash
python3 manage.py makemigrations && python3 manage.py migrate
```

## Running the server

You can start the Django server by running the following command line:

```bash
python3 manage.py runserver
```

If everything went OK, and you visit `127.0.0.1:8000` you will be able to see the app running

## Creating users

To create a superuser you can user the following command line and follo the instructions:

```bash
python3 manage.py createsupersuser
```

To create regular users you can use the sign up form from the app, or go to the Django admin panel in `127.0.0.1:8000/admin` and create one from the "Users" table.

# Why did I write this software?

I wanted to learn more about the full-stack experience in Django instead of using a front-end framework.

[Software Demo Video App](https://www.loom.com/share/323aaeb5655540ef8e1b750bfea87280?sid=28a6e19d-e24f-45e1-a666-3aa793cfc6ca)
[Code Demo Video App](https://www.loom.com/share/d8ea8601262c4d1889c9093a6c94eea7?sid=c5665b5c-11ac-4f49-b48b-5d4f7836de34)

# Web Pages

I created the following pages:

- Base page where I designed the footer and the navbar. This page is used in each child page
- The sign up page
- The login page
- The blog post page for each blog post, which is dynamically created
- The edit blog page
- The delete blog page
- Users can post comments in each post and delete them if they want
- Some specific information will be rendered in the pages just if you are an admin user

# Development Environment

## Development environment:

I used neovim as my code editor, tmux for a better workflow with my terminals, and linux with i3 as my OS.

## Tools

I used Python 3 as a programming language to develop this project, and the Django web framework.

# Useful Websites

I found the following websites useful to build my project:

- [Django's docs](https://docs.djangoproject.com/en/5.0/#django-documentation)
- [Tailwind CSS's docs](https://tailwindcss.com/docs/installation)
- [Blog post](https://learndjango.com/tutorials/django-login-and-logout-tutorial)

# Future Work

I will like to add the following thing

- I would like to make the website responsive. It's responsive in many parts, but not all of them are
- I would like to implement a prevent default so the website is not completely rendered every time that I submit a form
- I would like to avoid everyone being able to enter to the admin Django panel

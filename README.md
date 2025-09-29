📚 Library Management API

A practice project built with Django + Django REST Framework (DRF) to demonstrate Object-Oriented Programming (OOP) concepts in Python and Django.

This project implements models with inheritance, custom managers, serializers, ViewSets, custom actions, middleware, and signals — covering the most important OOP patterns in Django.

🚀 Features

Models (OOP in ORM)

BaseModel (abstract base class with timestamps)

Book (base model)

EBook & AudioBook (multi-table inheritance)

AvailableBook (proxy model)

BookManager (custom manager with .available())

Serializers

BookSerializer, EBookSerializer, AudioBookSerializer using ModelSerializer.

API Endpoints (ViewSets + Routers)

CRUD for Book, EBook, AudioBook.

Only authenticated users can access (IsAuthenticated).

Custom logic in create() → prevents duplicate book titles.

Custom action → POST /api/books/{id}/mark_unavailable/.

Middleware

Logs request method, path, user, and response status.

Saves logs to middleware_log.txt.

Signals

post_save signal on Book → prints "New Book Created: ".

🛠️ Tech Stack

Backend: Django 5, Django REST Framework

Database: SQLite (default, easy to swap for PostgreSQL/MySQL)

Auth: DRF session/token authentication

Logging: Custom middleware

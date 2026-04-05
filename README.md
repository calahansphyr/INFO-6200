# Personal Library Manager

A Python project implementing a modern Personal Library Manager with full web application architecture powered by Flask, SQLAlchemy, and Vercel. 

## Core Features
- **User Authentication:** Robust registration and login systems powered by `werkzeug.security`.
- **Data Privacy & Encryption:** Advanced Fernet encryption secures all string-based PII values (Title, Author, Genre) within the database (`cryptography`).
- **RESTful API Endpoint:** Export your owned list of books dynamically in JSON format.
- **Relational Database:** Stores structural ownership and data definitions via `Flask-SQLAlchemy`.

## Project Structure
- **web_app.py** — Main Flask application containing all User, Book, and API routes.
- **models.py** — SQLAlchemy Models mapping to our Relational Tables.
- **extensions.py** — Context initialization modules.
- **api/index.py** — Dedicated app entrypoint mapping for Vercel platform distributions.

## Local Installation / Setup

1. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

2. **Environment Variable Setup:**
Copy the template `.env.example` into a local `.env` and set your runtime variables.
```bash
cp .env.example .env
```
*(You will need to insert a live base64 Fernet key to successfully encrypt database models).*

3. **Running Locally (Development):**
```bash
python web_app.py
```
Then navigate to http://127.0.0.1:5000/ to access the application.

4. **Running Locally (Production WSGI Server - Gunicorn):**
```bash
gunicorn web_app:app
```

## Cloud Deployment (Vercel)

This application has been successfully hardened and formatted to deploy rapidly directly up into Vercel Serverless Pipelines.
Make sure you initialize the environmental `DATABASE_URI`, `SECRET_KEY`, and `ENCRYPTION_KEY` variables inside Vercel's remote Settings configurations.
The deployment behaves via the `vercel.json` configurations which points the standard endpoints over to the `@vercel/python` builder.

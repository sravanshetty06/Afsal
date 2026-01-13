# Absal (MR.Tech__077 CCTV) — Deployment Guide

This is a minimal Django site used as a static landing page. This README explains how to deploy it to Render (recommended) and configure environment variables and (optionally) a managed DB.

## Quick notes
- The app uses Django and Whitenoise to serve static files.
- By default, it uses a local SQLite DB (db.sqlite3). For production on Render, use a managed Postgres DB and set `DATABASE_URL`.
- `SECRET_KEY`, `DEBUG`, and `DATABASE_URL` are read from environment variables.

## Files added for deployment
- `Procfile` — start command for Render: `web: gunicorn Absal.wsgi --bind 0.0.0.0:$PORT`
- `.env.example` — sample environment variables (do not commit `.env` itself)
- `.gitignore` — ignores database, venvs, and secrets

---

## Deploying to Render (step-by-step)
1. Push this repository to GitHub.
2. Log in to Render (https://render.com) and create a new **Web Service**.
   - Connect your GitHub repo and pick the branch to deploy (e.g., `main`).
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start Command: `gunicorn Absal.wsgi --bind 0.0.0.0:$PORT`
   - Environment: `Python 3.x` (pick a stable supported version, e.g., 3.11/3.10)
3. Set environment variables on Render's dashboard for the new service:
   - `SECRET_KEY` — a long secret string
   - `DEBUG=False` — set to `False` in production
   - `ALLOWED_HOSTS` — optional (comma-separated), e.g. `myapp.onrender.com`
   - If using Postgres: `DATABASE_URL=postgres://user:pass@host:5432/dbname`
4. (Optional) Add a managed Postgres instance in Render and copy its DATABASE_URL to your Web Service env vars.
5. Deploy. After the first deploy, run migrations (you can use Render's Console or locally then push):
   - `python manage.py migrate`
   - `python manage.py createsuperuser` (optional)
6. The app will be accessible at the Render-provided domain (e.g., `https://<service>.onrender.com`).

## If you want **static-only** deployment instead
Because the site is a static HTML page, you can instead deploy the `templates/app1/index.html` as `index.html` to Vercel/Netlify (simpler & cheaper). If you want that, I can prepare a `public/` folder and config for Vercel/Netlify.

## Maintenance & Security
- Do **not** commit `.env` or `SECRET_KEY`. Keep them in Render's environment variables.
- Set `DEBUG=False` in production.
- Consider trimming `requirements.txt` to only packages you need to reduce build time.

---

If you want, I can now:
- Trim `requirements.txt` to essentials (Django, gunicorn, whitenoise, dj-database-url) to speed up builds.
- Add a small GitHub Actions workflow to run migrations after deploy.
- Create a `public/` static export for Netlify/Vercel.

Tell me which follow-up tasks you'd like me to do next.
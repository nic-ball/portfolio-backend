# Portfolio Backend

A Django-based REST API backend for a personal portfolio website. This application serves project data and handles contact form submissions.

## 🛠️ Technology Stack

- **Framework**: Django 5.2
- **API**: Django Rest Framework (DRF) 3.16
- **Database**: 
  - Development: SQLite
  - Production: PostgreSQL (via `dj-database-url`)
- **Server**: Gunicorn (Production), Django Dev Server (Development)
- **Utilities**: WhiteNoise (Static files), CORS Headers

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nic-ball/portfolio-backend.git
   cd portfolio-backend
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for Admin access):**
   ```bash
   python manage.py createsuperuser
   # Or use the utility script (uses env vars or defaults):
   python create_superuser.py
   ```

### Running the Application

Start the development server:
```bash
python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/`.

## ⚙️ Configuration

The application uses environment variables for configuration. Create a `.env` file in the root directory (optional for local dev, as defaults are provided in `settings.py` for non-production environments).

| Variable | Description | Default (Dev) |
|----------|-------------|---------------|
| `SECRET_KEY` | Django secret key | `django-insecure...` |
| `DEBUG` | Enable debug mode | `True` (unless `RENDER` env var is present) |
| `DATABASE_URL` | Database connection string | `sqlite:///db.sqlite3` |
| `RENDER` | Set to distinct Prod from Dev | `None` |
| `RENDER_EXTERNAL_HOSTNAME`| Hostname for `ALLOWED_HOSTS` | `None` |
| `DJANGO_SUPERUSER_USERNAME`| Admin username for script | `admin` |
| `DJANGO_SUPERUSER_PASSWORD`| Admin password for script | `thisIsNotTheWay69!` |

## 📖 API Reference

### Projects

#### List all Projects
**GET** `/api/projects/`

Returns a list of portfolio projects sorted by newest first.

**Response Example:**
```json
[
    {
        "id": 1,
        "title": "My Awesome Project",
        "description": "A cool web app built with Django.",
        "technologies": "Python, Django, React",
        "github_link": "https://github.com/user/project",
        "live_link": "https://project.com",
        "image_url": "https://example.com/image.jpg",
        "created_at": "2023-10-27T10:00:00Z"
    }
]
```

### Contact

#### Send a Message
**POST** `/api/contact/`

Submits a contact form message. In development, this prints to the console. In production, it can be configured to send emails.

**Request Body:**
```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Hi, I'd like to hire you!"
}
```

**Response Example (Success):**
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Hi, I'd like to hire you!",
    "created_at": "2023-10-27T10:05:00Z"
}
```

## 📦 Deployment

This project is configured for deployment on [Render](https://render.com/).

- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn backend.wsgi:application`

See `build.sh` for the build steps (installs deps, collects static files, migrates DB, creates superuser).

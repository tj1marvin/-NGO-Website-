# NGO Website Deployment Guide

## Deployment Steps

### 1. Environment Setup

Set up environment variables in `.env`:
```
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost:5432/ngo_db
```

### 2. Production Database

Switch to PostgreSQL:
```bash
pip install psycopg2-binary
```

### 3. Gunicorn Setup

```bash
pip install gunicorn
gunicorn ngo_project.wsgi:application --bind 0.0.0.0:8000
```

### 4. Nginx Configuration

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        alias /path/to/staticfiles/;
    }

    location /media/ {
        alias /path/to/media/;
    }
}
```

### 5. SSL Certificate

Install certbot:
```bash
sudo apt-get install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

### 6. Systemd Service

Create `/etc/systemd/system/ngo-django.service`:
```ini
[Unit]
Description=NGO Django Service
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/ngo_project
ExecStart=/path/to/venv/bin/gunicorn ngo_project.wsgi:application --bind 0.0.0.0:8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Start service:
```bash
sudo systemctl start ngo-django
sudo systemctl enable ngo-django
```

## Docker Deployment

### Dockerfile

```dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "ngo_project.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### Build and Run

```bash
docker build -t ngo-website .
docker run -p 8000:8000 ngo-website
```

## Backup and Maintenance

### Database Backup

```bash
python manage.py dumpdata > backup.json
```

### Database Restore

```bash
python manage.py loaddata backup.json
```

## Monitoring

Monitor application logs:
```bash
tail -f /var/log/ngo-django.log
```

Monitor with Gunicorn:
```bash
gunicorn ngo_project.wsgi --bind 0.0.0.0:8000 --workers 4 --log-level debug
```

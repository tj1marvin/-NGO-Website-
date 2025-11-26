#!/bin/bash

# NGO Django Project Setup Script

echo "🚀 Starting NGO Django Project Setup..."

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p media
mkdir -p static
mkdir -p staticfiles

# Run migrations
echo "🗄️  Running migrations..."
python manage.py migrate

# Create superuser
echo "👤 Creating superuser..."
python manage.py createsuperuser

# Collect static files
echo "📚 Collecting static files..."
python manage.py collectstatic --noinput

echo "✅ Setup complete!"
echo "🎉 To start the server, run: python manage.py runserver"
echo "📊 Visit http://localhost:8000/ to access the application"
echo "🔐 Admin panel: http://localhost:8000/admin/"

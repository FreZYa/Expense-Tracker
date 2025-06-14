# Expense Tracker

A Django-based expense tracking application.

## Setup

1. Install Python dependencies:
```bash
pip install django
```

2. Run migrations:
```bash
make mig
```

3. Create migration files:
```bash
make mm
```

4. Create superuser:
```bash
make createsuperuser
```

5. Run the development server:
```bash
make run
```

## Available Commands

- `make run` - Start Django development server
- `make mig` - Run database migrations
- `make mm` - Make database migrations
- `make shell` - Open Django shell
- `make createsuperuser` - Create admin user

## Access

- Development server: http://127.0.0.1:8000
- Admin panel: http://127.0.0.1:8000/admin 
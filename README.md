<p align="center">
    <a href="https://github.com/M4hbod/GiftX">
        <img src="./docs/logo.svg" alt="GiftX Logo" width="128"/>
    </a>
</p>

# GiftX - Digital Gift Card Platform

GiftX is a Django-based web application for buying digital gift cards. The platform allows users to browse different gift card categories and purchase gift cards.

## Features

- User authentication with email and phone number
- Browse gift cards by categories
- Admin interface for managing gift cards and users

## Prerequisites

- Python 3.12+
- Django 5.2+
- Pillow for image handling
- uv for package management

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/GiftX.git
cd GiftX
```

2. Create a virtual environment:
```bash
uv sync
```

3. Apply migrations:
```bash
make migrate
```

4. Create a superuser:
```bash
make createsuperuser
```

5. Run the development server:
```bash
make run
```

## Project Structure

- `users/` - Custom user authentication app
- `gift_cards/` - Gift card management app
- `core/` - Core functionality and home page
- `config/` - Project settings and configuration
- `templates/` - Base templates and shared components

## Development

The project uses several development tools:

- Ruff for code formatting and linting
- Django Stubs for type checking
- Make commands for common tasks

### Available Make Commands

```bash
make migrations    # Create new database migrations
make migrate       # Apply database migrations
make run           # Run development server
make shell         # Open Django shell
make superuser     # Create a superuser
```

# Django Ninja Docker Test

Minimal Django Ninja app for Docker deployment testing.

## Endpoints
- `GET /`
- `GET /api/hello`
- `POST /api/message`
- `GET /api/docs`

## Docker
```bash
docker build -t django-ninja-test:latest .
docker run -d --name django-ninja-test -p 8000:8000 django-ninja-test:latest
```

from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# CORE
# =========================================================

# Em produção (Vercel), use SECRET_KEY em variável de ambiente
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-change-me")

# DEBUG: local = 1 | produção = 0
DEBUG = os.getenv("DEBUG", "0") == "1"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    ".vercel.app",
]

# Necessário para POST/Forms na Vercel (CSRF)
CSRF_TRUSTED_ORIGINS = [
    "https://*.vercel.app",
]

# Corrige HTTPS atrás do proxy da Vercel
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# =========================================================
# APPS
# =========================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "home",
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================================================
# URLS / WSGI
# =========================================================

ROOT_URLCONF = "pweb.urls"
WSGI_APPLICATION = "pweb.wsgi.application"


# =========================================================
# TEMPLATES
# =========================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # se tiver templates globais, coloque aqui
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# =========================================================
# DATABASE
# =========================================================

# 🔹 Banco local (SQLite)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 🔹 Produção (Vercel + Neon)
# Prioridade CORRETA das variáveis
DATABASE_URL = (
    os.getenv("DATABASE_URL_UNPOOLED")       # ✅ migrations / sem pooler
    or os.getenv("POSTGRES_URL_NON_POOLING")
    or os.getenv("DATABASE_URL")              # pooler
    or os.getenv("POSTGRES_URL")
)

if DATABASE_URL:
    DATABASES["default"] = dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=0,        # 🔥 ESSENCIAL em serverless (Vercel)
        ssl_require=True,
    )


# =========================================================
# PASSWORD VALIDATION
# =========================================================

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# =========================================================
# INTERNATIONALIZATION
# =========================================================

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Fortaleza"
USE_I18N = True
USE_TZ = True


# =========================================================
# STATIC FILES
# =========================================================

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =========================================================
# PRODUÇÃO: SEGURANÇA
# =========================================================

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # ⚠️ Em Vercel pode causar loop se algo estiver errado,
    # mas normalmente funciona bem
    SECURE_SSL_REDIRECT = True

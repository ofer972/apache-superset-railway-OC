import os

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

ENABLE_PROXY_FIX = True

SECRET_KEY = os.environ.get("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE")

HTML_SANITIZATION = False

###AUTH_ROLE_PUBLIC = 'Public'
###PUBLIC_ROLE_LIKE = 'Gamma'
###PUBLIC_ROLE_LIKE_GAMMA = True


# 1. Enable Flask-Talisman (if not already enabled elsewhere)
TALISMAN_ENABLED = True

# 2. Define Talisman configuration (REMOVED session keys from here)
TALISMAN_CONFIG = {
    "content_security_policy": {
        "default-src": ["'self'"],
        "img-src": ["*", "data:"],
        "worker-src": ["'self'", "blob:"],
        "connect-src": ["'self'", "https://api.mapbox.com", "https://events.mapbox.com"],
        "script-src": ["'self'", "'strict-dynamic'"],
        "style-src": ["'self'", "'unsafe-inline'"],
        "frame-ancestors": [
            "'self'",
            "https://dashboards-production-6a67.up.railway.app", # <-- *** REMEMBER TO REPLACE THIS ***
            "http://localhost:8050",                             # Added for local development
            "http://127.0.0.1:8050"                              # Added for local development
        ],
    },
    "content_security_policy_nonce_in": ["script-src"],
    "force_https": True,
    "strict_transport_security": True,
    # REMOVED: "session_cookie_secure": False,
    # REMOVED: "session_cookie_httponly": True,
    "frame_options": None, # Disable X-Frame-Options
    "frame_options_allow_from": None,
}

# 3. Add Flask Session Cookie Settings (outside TALISMAN_CONFIG)
SESSION_COOKIE_HTTPONLY = True  # Prevent JavaScript access to the session cookie
SESSION_COOKIE_SECURE = True   # Set to True if Superset is ONLY served over HTTPS

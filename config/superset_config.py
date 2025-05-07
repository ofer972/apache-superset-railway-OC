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

# 2. Define Talisman configuration
TALISMAN_CONFIG = {
    "content_security_policy": {
        # Base policy: restrict to self by default
        "default-src": ["'self'"],
        # Allow images from anywhere and data URIs
        "img-src": ["*", "data:"],
        # Allow web workers from self and blob URIs
        "worker-src": ["'self'", "blob:"],
        # Allow connections to self and specific external services if needed (e.g., Mapbox)
        "connect-src": ["'self'", "https://api.mapbox.com", "https://events.mapbox.com"],
        # Allow scripts from self and dynamically added nonces
        "script-src": ["'self'", "'strict-dynamic'"],
        # Allow inline styles and styles from self
        "style-src": ["'self'", "'unsafe-inline'"],

        # --- THIS IS THE IMPORTANT PART ---
        # Allow embedding only by 'self' (Superset itself) and your Dash app's domain
        "frame-ancestors": [
            "'self'",
            "https://dashboards-production-6a67.up.railway.app" # <-- *** REPLACE THIS *
        ],
        # ----------------------------------
    },
    # Add nonce for script-src if using 'strict-dynamic'
    "content_security_policy_nonce_in": ["script-src"],

    # Adjust these based on your deployment environment (behind proxy, HTTPS, etc.)
    "force_https": False,
    "strict_transport_security": False,
    "session_cookie_secure": False, # Set to True if Superset is served over HTTPS
    "session_cookie_httponly": True,

    # IMPORTANT: Disable the default X-Frame-Options when using frame-ancestors
    "frame_options": None,
    "frame_options_allow_from": None,
}

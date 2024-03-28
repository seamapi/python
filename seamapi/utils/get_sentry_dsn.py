import os

def get_sentry_dsn():
  # This is replaced with a hard-coded value during the build process (see scripts/prebuild.py)
  return os.environ.get("SENTRY_DSN", None)
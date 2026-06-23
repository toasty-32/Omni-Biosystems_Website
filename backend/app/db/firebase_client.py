from functools import lru_cache
import firebase_admin
from firebase_admin import credentials, firestore as firebase_firestore
from app.core.config import settings


@lru_cache(maxsize=1)
def get_firebase_app() -> firebase_admin.App:
    if firebase_admin._apps:
        return firebase_admin.get_app()
    # On Cloud Run, Application Default Credentials are used automatically.
    # Locally, set GOOGLE_APPLICATION_CREDENTIALS to a service account key file.
    cred = credentials.ApplicationDefault()
    return firebase_admin.initialize_app(cred, {'projectId': settings.firebase_project_id})


def get_db() -> firebase_firestore.firestore.Client:
    get_firebase_app()
    return firebase_firestore.client()

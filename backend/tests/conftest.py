"""
Stub out firebase_admin and google-auth before any test module imports them.
This prevents the broken system cryptography package from being loaded in
environments where _cffi_backend is unavailable (e.g. this dev container).
On CI (GitHub Actions, Python 3.12) the real packages are used and work fine.
"""
import sys
from unittest.mock import MagicMock

_FIREBASE_MOCKS = [
    'firebase_admin',
    'firebase_admin.credentials',
    'firebase_admin.auth',
    'firebase_admin.firestore',
    'google',
    'google.auth',
    'google.auth.credentials',
    'google.auth.transport',
    'google.auth.transport.requests',
    'google.cloud',
    'google.cloud.firestore',
    'google.oauth2',
    'google.oauth2.service_account',
]

for _mod in _FIREBASE_MOCKS:
    if _mod not in sys.modules:
        sys.modules[_mod] = MagicMock()

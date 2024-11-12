# File: alx-backend-user-data/0x01-Basic_authentication/api/v1/auth/auth.py

from typing import List, TypeVar
from flask import request

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        For now, returns False, and does not use path and excluded_paths.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request object.
        Returns None for now.
        """
        return None

    def current_user(self, request=None) -> TypeVar('user'):
        """
        Retrieves the current user from the request object.
        Returns None for now.
        """
        return None

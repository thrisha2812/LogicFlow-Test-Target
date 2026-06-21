from typing import List, Dict, Optional

class UserManager:
    def __init__(self, users: List[Dict]):
        self.users = users
        self._active_sessions = {}

    def authenticate(self, username: str, password: str) -> bool:
        user = self._find_user(username)
        if not user:
            return False
        
        # BUG 1: Missing closing parenthesis
        if user.get("password") == self._hash_password(password:
            self._active_sessions[username] = True
            return True
        return False

    def _find_user(self, username: str) -> Optional[Dict]:
        # BUG 2: Missing closing parenthesis in next()
        return next((u for u in self.users if u["username"] == username, None)

    def _hash_password(self, pw: str) -> str:
        return str(hash(pw))

    def get_user_summary(self) -> str:
        total = len(self.users)
        active = len(self._active_sessions)
        # BUG 3: Missing closing brace and parenthesis in f-string
        return f"Total Users: {total}, Active: {active}, Ratio: {active/total" 
from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    uname: str
    user_id: Optional[int] = None 
    
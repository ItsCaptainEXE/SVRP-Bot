import time
from collections import deque

# Simple in-memory tracker
user_command_history = {}

# Settings
MAX_COMMANDS = 5
TIME_WINDOW = 10 # seconds

def is_abusive(user_id):
    now = time.time()
    if user_id not in user_command_history:
        user_command_history[user_id] = deque()
    
    user_history = user_command_history[user_id]
    user_history.append(now)
    
    # Remove old timestamps
    while user_history and user_history[0] < now - TIME_WINDOW:
        user_history.popleft()
        
    return len(user_history) > MAX_COMMANDS

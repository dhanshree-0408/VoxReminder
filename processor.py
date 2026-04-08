import dateparser
from datetime import datetime, timedelta
import re

def extract_info(text):
    text = text.lower().strip()
    
    # 1. Task Extraction
    clean_text = re.sub(r'^(remind me to|remind me about|remind me)\s+', '', text)
    parts = re.split(r'\s+(at|in|on|tomorrow|today)\s+', clean_text, maxsplit=1)
    task = parts[0].strip().capitalize() if parts else "Reminder"

    # 2. Time Parsing
    now = datetime.now()
    settings = {
        'PREFER_DATES_FROM': 'future',
        'RELATIVE_BASE': now,
        'RETURN_AS_TIMEZONE_AWARE': False
    }
    
    target_time = dateparser.parse(text, settings=settings)
    
    # Fix for "in X minutes" specifically
    if "in " in text and "minute" in text:
        nums = re.findall(r'\d+', text)
        mins = int(nums[0]) if nums else 1
        target_time = now + timedelta(minutes=mins)
        
    return task, target_time
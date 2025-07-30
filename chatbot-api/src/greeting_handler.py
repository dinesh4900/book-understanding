# src/greeting_handler.py

import random
import re

def is_greeting(message):
    """Check if the message contains a greeting."""
    greeting_patterns = [
        r'\b(hi|hello|hey|hiya|howdy)\b',
        r'\b(good\s+(morning|afternoon|evening|day))\b',
        r'\b(what\'s\s+up|whats\s+up|sup)\b',
        r'\b(how\s+(are\s+you|r\s+u))\b',
        r'\b(greetings|salutations)\b',
    ]
    
    message_lower = message.lower().strip()
    for pattern in greeting_patterns:
        if re.search(pattern, message_lower, re.IGNORECASE):
            return True
    return False

def is_simple_greeting(message):
    """Check if message is ONLY a greeting (no other content)."""
    message_lower = message.lower().strip()
    cleaned = re.sub(r'[^\w\s]', '', message_lower)
    words = cleaned.split()
    
    # If very short and contains greeting
    if len(words) <= 3 and is_greeting(message):
        return True
    return False

def get_greeting_response(message=""):
    """Generate a random greeting response."""
    responses = [
        "Hello! 👋 I'm your book assistant. Ask me anything about the book!",
        "Hi there! 😊 Ready to explore the book together?", 
        "Hey! 📚 I'm here to help you understand the book better.",
        "Hello! 🤖 What would you like to know about the book?",
        "Hi! ✨ I can answer questions about the book content.",
        "Greetings! 📖 Let's dive into the book. What interests you?",
        "Hello there! 🌟 Ask me about characters, plot, or anything in the book!",
        "Hi! 💡 I'm your AI book companion. How can I help?",
        "Hey! 🔍 Ready to discover what's in the book?",
        "Hello! 🎉 I'm excited to discuss the book with you!",
    ]
    
    # Special responses for time-specific greetings
    message_lower = message.lower()
    if 'morning' in message_lower:
        morning_responses = [
            "Good morning! ☀️ Ready to start the day with some book exploration?",
            "Morning! 🌅 Let's discover something new in the book today!",
            "Good morning! 📚 What shall we explore in the book today?",
        ]
        return random.choice(morning_responses)
    elif 'afternoon' in message_lower:
        afternoon_responses = [
            "Good afternoon! ☀️ Perfect time for book discussion!",
            "Afternoon! 📖 How can I help with the book today?",
            "Good afternoon! 🌞 Ready to continue our book journey?",
        ]
        return random.choice(afternoon_responses)
    elif 'evening' in message_lower:
        evening_responses = [
            "Good evening! 🌙 Great time for thoughtful book conversation!",
            "Evening! ✨ Let's explore what the book teaches us tonight.",
            "Good evening! 📚 Perfect for diving into the book!",
        ]
        return random.choice(evening_responses)
    
    return random.choice(responses)

"""
CipherForge — Encryption Engine
================================
Author: [Your Name]
Date: 2026

This file contains my custom 5-layer encryption algorithm.

PHASES:
  1. Substitution — Replace characters with different ones
  2. Transposition — Rearrange the order of characters  
  3. Key-Dependent — Make output depend on a secret password
  4. Noise Injection — Add fake characters to confuse attackers
  5. Wild Card — My unique invention!

RULES:
  - encrypt() MUST be reversible
  - decrypt(encrypt(message)) MUST return the original message
"""

def phase1_encrypt(text, key):
  shift = key.get("shift", 5)
  
  result = ""
  for char in text:
    if 32 <= ord(char) <= 126:
      position = ord(char) - 32
      new_position = (position + shift) % 95
      result += chr(new_position + 32)
    else:
      result += char
      
  return result

def phase1_decrypt(text, key):
  shift = key.get("shift", 5)
  
  result = ""
  for char in text: 
    if 32 <= ord(char) <= 126:
      position = ord(char) - 32
      new_position = (position - shift) % 95
      result += chr(new_position + 32)
    else:
      result += char
  
  return result

def encrypt(text, key):
    """Master encrypt — all 5 phases."""
    result = phase1_encrypt(text, key)
    result = phase2_encrypt(result, key)
    result = phase3_encrypt(result, key)
    result = phase4_encrypt(result, key)
    result = phase5_encrypt(result, key)
    return result

def decrypt(text, key):
    """Master decrypt — reverse all phases."""
    result = text
    result = phase5_decrypt(result, key)
    result = phase4_decrypt(result, key)
    result = phase3_decrypt(result, key)
    result = phase2_decrypt(result, key)
    result = phase1_decrypt(result, key)
    return result
  
def phase2_encrypt(text, key):
  block_size = key.get("block_size", 4)
  result = ""
  
  for i in range(0, len(text), block_size):
    block = text[i:i + block_size]
    result += block[::-1]
  
  return result

def phase2_decrypt(text, key):
  block_size = key.get("block_size", 4)
  result = ""
  
  for i in range(0, len(text), block_size):
    block = text[i:i + block_size]
    result += block[::-1]
    
  return result

def phase3_encrypt(text, key):
  password = key.get("password", "SECRET")
  result = ""
  
  for i, char in enumerate(text):
    if 32 <= ord(char) <= 126:
      password_char = password[i % len(password)]
      password_shift = ord(password_char) % 95
      
      position = ord(char) - 32
      new_position = (position + password_shift) % 95
      result += chr(new_position + 32)
    else:
      result += char
  return result

def phase3_decrypt(text, key):
    """
    Phase 3: Reverse the password-dependent encryption.
    
    CRITICAL: Must use the SAME password that was used for encryption!
    Wrong password = garbage output.
    
    Args:
        text: The encrypted string
        key: Dictionary with the SAME password used for encryption
        
    Returns:
        The decrypted string (if password is correct)
    """
    password = key.get("password", "SECRET")
    
    result = ""
    
    for i, char in enumerate(text):
        if 32 <= ord(char) <= 126:
            # Get same password character for this position
            password_char = password[i % len(password)]
            password_shift = ord(password_char) % 95
            
            # SUBTRACT the shift to reverse encryption
            position = ord(char) - 32
            new_position = (position - password_shift) % 95
            result += chr(new_position + 32)
        else:
            result += char
    
    return result
  
def phase4_encrypt(text, key):
    """Insert noise character every N positions."""
    interval = key.get("noise_interval", 3)
    noise = key.get("noise_char", "~")
    
    result = ""
    count = 0
    
    for char in text:
        result += char
        count += 1
        # Insert noise after every N real characters
        if count % interval == 0:
            result += noise
    
    return result


def phase4_decrypt(text, key):
    """Remove noise characters at their known positions."""
    interval = key.get("noise_interval", 3)
    
    result = ""
    real_count = 0
    i = 0
    
    while i < len(text):
        result += text[i]
        real_count += 1
        i += 1
        
        # Skip the noise character after every N real characters
        if real_count % interval == 0 and i < len(text):
            i += 1  # Skip noise
    
    return result
  
def phase5_encrypt(text, key):
    """Swap adjacent character pairs."""
    # Handle empty and single-character strings
    if len(text) <= 1:
        return text
    
    result = ""
    
    for i in range(0, len(text) - 1, 2):
        # Swap pairs: AB → BA
        result += text[i + 1]
        result += text[i]
    
    # Handle odd-length strings (last char stays)
    if len(text) % 2 == 1:
        result += text[-1]
    
    return result


def phase5_decrypt(text, key):
    """Swapping twice returns original — self-inverse!"""
    return phase5_encrypt(text, key)  # Same operation!
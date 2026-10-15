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
    # TODO: Phases 2-5
    return result

def decrypt(text, key):
    """Master decrypt — reverse all phases."""
    result = text
    # TODO: Phases 5-2
    result = phase1_decrypt(result, key)
    return result


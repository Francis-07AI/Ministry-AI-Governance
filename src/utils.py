"""Utility functions for the Ministry AI Governance Assistant."""

import os
import re
from typing import List, Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Risk flag keywords
RISK_FLAGS = {
    "PASTORAL_CARE": ["counseling", "therapy", "depression", "suicide", "mental health"],
    "CHILD_SAFETY": ["child", "minor", "youth", "kid", "teen", "student"],
    "FINANCIAL_MANIPULATION": ["donor targeting", "giving patterns", "maximize donations", "increase giving"],
    "DATA_BOUNDARY": ["analyze database", "member data", "private information", "church records"],
    "THEOLOGICAL": ["should we believe", "is it biblical", "theological position", "doctrinal"],
    "PASTORAL_CONTENT": ["write sermon", "create prayer", "generate liturgy", "write homily"]
}

def detect_risk_flags(query: str) -> List[str]:
    """Detect risk flags in user query."""
    flags = []
    query_lower = query.lower()
    
    for flag_type, keywords in RISK_FLAGS.items():
        if any(keyword in query_lower for keyword in keywords):
            flags.append(flag_type)
    
    return flags

def sanitize_query(query: str) -> str:
    """Remove PII and sensitive information from query."""
    # Remove email addresses
    query = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL]', query)
    
    # Remove phone numbers
    query = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', '[PHONE]', query)
    
    # Remove SSN patterns
    query = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '[SSN]', query)
    
    return query

def get_api_key(service: str) -> str:
    """Get API key from environment."""
    key = os.getenv(f"{service.upper()}_API_KEY")
    if not key:
        raise ValueError(f"{service} API key not found in .env file")
    return key

def format_sources(sources: List[Dict[str, Any]]) -> str:
    """Format source citations for display."""
    if not sources:
        return "No sources cited."
    
    formatted = "\n\nSources:\n"
    for i, source in enumerate(sources, 1):
        formatted += f"{i}. {source.get('title', 'Unknown')} - {source.get('url', 'No URL')}\n"
    
    return formatted

def add_disclaimers(response: str, risk_flags: List[str]) -> str:
    """Add appropriate disclaimers based on risk flags."""
    disclaimers = []
    
    # General disclaimer (always included)
    disclaimers.append(
        "\n\n---\nDisclaimer: This guidance is for informational purposes. "
        "Consult your denominational resources and professional advisors for implementation."
    )
    
    # Specific disclaimers
    if "PASTORAL_CARE" in risk_flags:
        disclaimers.append(
            "\n IMPORTANT: This system cannot provide counseling. "
            "Please consult a qualified pastoral counselor or mental health professional."
        )
    
    if "CHILD_SAFETY" in risk_flags:
        disclaimers.append(
            "\n CHILD SAFETY: Questions involving children require expert guidance. "
            "Consult child protection specialists and legal counsel."
        )
    
    if "THEOLOGICAL" in risk_flags:
        disclaimers.append(
            "\n THEOLOGICAL: This system does not provide theological or doctrinal guidance. "
            "Consult your pastor or denominational resources."
        )
    
    if "PASTORAL_CONTENT" in risk_flags:
        disclaimers.append(
            "\n PASTORAL CONTENT: Sermon preparation requires pastoral calling, study, and prayer. "
            "AI should only assist with research, not replace your own work."
        )
    
    return response + "".join(disclaimers)
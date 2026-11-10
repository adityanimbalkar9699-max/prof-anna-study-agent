"""
Academic Configuration, Typography Tokens & Aesthetic Standards for Prof. Anna
"""

from dataclasses import dataclass
from typing import Dict, Any

# Anti-AI Aesthetic Color Palette (No generic purple gradients, no sterile harsh black)
PALETTE = {
    "bg_light": "#FAF9F6",         # Warm Alabaster / Ivory
    "bg_dark": "#09090B",          # Rich Obsidian
    "surface_light": "#FFFFFF",
    "surface_dark": "#121316",
    "text_primary_light": "#0F172A", # Deep Slate / Rich Charcoal
    "text_primary_dark": "#F8FAFC",
    "text_secondary_light": "#475569",
    "text_secondary_dark": "#94A3B8",
    "border_light": "#E2E8F0",
    "border_dark": "#27272A",
    "accent_primary": "#0D9488",   # Refined Teal / Academic Jade
    "accent_gold": "#D97706",      # Editorial Amber / Gold
    "accent_blue": "#2563EB",      # Cobalt Scholar Blue
    "accent_crimson": "#DC2626",   # Critical / Alert
    "accent_emerald": "#059669",   # Verified Pass
}

# Editorial Typography Scales
TYPOGRAPHY = {
    "font_title": "Helvetica-Bold",
    "font_body": "Helvetica",
    "font_mono": "Courier",
    "tracking_title": -0.02,
    "tracking_caption": 0.04,
}

# SIH (Smart India Hackathon) Evaluation Weightings
SIH_RUBRIC_WEIGHTS = {
    "problem_severity_clarity": 0.15,
    "novelty_uniqueness": 0.20,
    "feasibility_technical_depth": 0.25,
    "business_model_impact": 0.15,
    "prototype_readiness": 0.15,
    "presentation_cadence": 0.10,
}

# Default Academic Universities / Syllabus Presets
UNIVERSITY_PRESETS = {
    "SPPU": "Savitribai Phule Pune University (2019/2024 Scheme)",
    "MU": "Mumbai University (Rev-2019/2023 C-Scheme)",
    "VTU": "Visvesvaraya Technological University (2021/2022 Scheme)",
    "AnnaUniv": "Anna University (Regulation 2021)",
    "AKTU": "Dr. A.P.J. Abdul Kalam Technical University (NEP Scheme)",
    "General_Engineering": "Standard IEEE/ABET Engineering Curriculum",
}

"""
Mnemonic & Spatial Memory Palace (Method of Loci) Studio
========================================================
Converts complex academic lists, legal articles, anatomical pathways,
and mathematical formulas into high-retention phonetic mnemonics and
vivid spatial Memory Palace journeys ("Smart Work over Hard Work").
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional


@dataclass
class MemoryPalaceRoom:
    room_name: str
    physical_anchor: str
    concept_to_remember: str
    vivid_sensory_story: str
    exam_cue: str


@dataclass
class MnemonicPackage:
    topic: str
    phonetic_acronym: str
    breakdown: Dict[str, str]
    rhyming_or_story_hook: str
    memory_palace_rooms: List[MemoryPalaceRoom]
    examiner_recall_secret: str


PRESET_MNEMONICS = {
    "upsc_schedules": MnemonicPackage(
        topic="12 Schedules of Indian Constitution",
        phonetic_acronym="TEARS OF OLD PM",
        breakdown={
            "T": "Territory (1st Schedule - States & Union Territories)",
            "E": "Emoluments & Salaries (2nd Schedule - President, Judges, Governors)",
            "A": "Affirmations & Oaths (3rd Schedule)",
            "R": "Rajya Sabha Seat Allocation (4th Schedule)",
            "S": "Scheduled Areas Administration (5th Schedule)",
            "O": "Other Tribal Areas - Assam, Meghalaya, Tripura, Mizoram (6th Schedule)",
            "F": "Federal Lists - Union, State, Concurrent (7th Schedule)",
            "O": "Official Languages - 22 Languages (8th Schedule)",
            "L": "Land Reforms & Validation of Acts (9th Schedule)",
            "D": "Defection Law - Anti-Defection 52nd Amendment (10th Schedule)",
            "P": "Panchayats 73rd Amendment (11th Schedule - 29 items)",
            "M": "Municipalities 74th Amendment (12th Schedule - 18 items)",
        },
        rhyming_or_story_hook="Tears of an Old Prime Minister remembering all 12 pillars of the Republic.",
        memory_palace_rooms=[
            MemoryPalaceRoom("1. Grand Front Gate", "Map on the Gate", "Territory (1st)", "A giant brass map of India swinging on the front gates.", "Schedule 1: Borders"),
            MemoryPalaceRoom("2. Entry Foyer", "Gold Money Safe", "Emoluments (2nd)", "A stack of gold bars and salary cheques for the President on the marble counter.", "Schedule 2: Pay"),
            MemoryPalaceRoom("3. Living Room", "Hand on the Holy Book", "Oaths (3rd)", "Ministers raising their right hands taking a solemn oath before the fireplace.", "Schedule 3: Oath"),
        ],
        examiner_recall_secret="UPSC Prelims always mixes 5th and 6th Schedules. Remember 6th is specifically 'AMTM' (Assam, Meghalaya, Tripura, Mizoram).",
    ),
    "cranial_nerves": MnemonicPackage(
        topic="12 Cranial Nerves in Order (Anatomy / NEET)",
        phonetic_acronym="OOOTTAFAGVSH",
        breakdown={
            "O": "I - Olfactory (Smell)",
            "O": "II - Optic (Vision)",
            "O": "III - Oculomotor (Eye movement, pupil)",
            "T": "IV - Trochlear (Superior oblique muscle)",
            "T": "V - Trigeminal (Facial sensation, mastication)",
            "A": "VI - Abducens (Lateral rectus)",
            "F": "VII - Facial (Expressions, taste anterior 2/3)",
            "A": "VIII - Vestibulocochlear / Auditory (Hearing, balance)",
            "G": "IX - Glossopharyngeal (Taste posterior 1/3, swallowing)",
            "V": "X - Vagus (Parasympathetic viscera, heart rate)",
            "S": "XI - Spinal Accessory (Sternocleidomastoid, trapezius)",
            "H": "XII - Hypoglossal (Tongue movement)",
        },
        rhyming_or_story_hook="Oh, Oh, Oh, To Touch And Feel A Good Velvet, Such Heaven!",
        memory_palace_rooms=[
            MemoryPalaceRoom("1. Bedroom Mirror", "Giant Perfume Bottle", "Olfactory (CN I)", "Spraying sweet lavender perfume right into your nose.", "Smell test"),
            MemoryPalaceRoom("2. Window Balcony", "Telescope", "Optic (CN II)", "Looking through a golden telescope watching an eagle fly.", "Visual acuity"),
        ],
        examiner_recall_secret="NEET Trap: CN III, IV, VI control eye muscles ('LR6 SO4 remainder 3' - Lateral Rectus VI, Superior Oblique IV, all others III).",
    ),
    "accounting_golden_rules": MnemonicPackage(
        topic="Golden Rules of Double-Entry Bookkeeping (Commerce / CA)",
        phonetic_acronym="RPN (Real, Personal, Nominal)",
        breakdown={
            "Real Account": "Debit what comes in, Credit what goes out (Assets, Cash, Machinery)",
            "Personal Account": "Debit the receiver, Credit the giver (Individuals, Companies, Debtors/Creditors)",
            "Nominal Account": "Debit all expenses and losses, Credit all incomes and gains (Salaries, Rent, Sales)",
        },
        rhyming_or_story_hook="Real assets roll in, People receive and give, Nominal costs we live.",
        memory_palace_rooms=[
            MemoryPalaceRoom("1. Warehouse Loading Dock", "Forklift unloading cash", "Real Accounts", "Brand new factory machinery arriving through the roll-up door (Debit in).", "Asset purchases"),
            MemoryPalaceRoom("2. Manager Office", "Client shaking hands", "Personal Accounts", "The CEO handing a signed cheque to the client who receives it (Debit Receiver).", "Debtor settlement"),
            MemoryPalaceRoom("3. Coffee Breakroom", "Billboard of receipts and profits", "Nominal Accounts", "Red receipts tacked to the wall (Debit expense), glowing green revenue graphs (Credit income).", "P&L Statement"),
        ],
        examiner_recall_secret="CA Foundation Trap: Outstanding expense is NOT a nominal account; it is a Representative Personal Account!",
    ),
}


class MemoryPalaceStudio:
    """
    World-class mnemonic generator and spatial memory palace constructor.
    """

    def construct(self, topic: str) -> MnemonicPackage:
        l_top = topic.lower()

        # Check presets
        if any(w in l_top for w in ["schedule", "constitution", "polity", "tears"]):
            return PRESET_MNEMONICS["upsc_schedules"]
        elif any(w in l_top for w in ["cranial", "nerve", "neet", "anatomy"]):
            return PRESET_MNEMONICS["cranial_nerves"]
        elif any(w in l_top for w in ["golden rule", "accounting", "debit", "credit", "ledger"]):
            return PRESET_MNEMONICS["accounting_golden_rules"]

        # Dynamic synthesis for any topic
        words = topic.split()
        initials = "".join([w[0].upper() for w in words])[:6] or "SMART"
        return MnemonicPackage(
            topic=topic.title(),
            phonetic_acronym=initials,
            breakdown={
                char: f"Key Dimension {i+1} of {topic}: Fundamental invariant property and application."
                for i, char in enumerate(initials)
            },
            rhyming_or_story_hook=f"The smart mnemonic anchor for rapid recall of {topic}.",
            memory_palace_rooms=[
                MemoryPalaceRoom("Room 1: The Grand Archway", "Glowing Blueprint", "Foundation", f"Enter the archway and touch the glowing stone inscribed with the core theorem of {topic}.", "Initial definition"),
                MemoryPalaceRoom("Room 2: The Core Laboratory", "Interactive Mechanism", "Working Principle", f"In the center of the lab, a frictionless mechanism executes the step-by-step transformation of {topic}.", "Derivation / Flow"),
                MemoryPalaceRoom("Room 3: The Hall of Records", "Gold Plaque", "Final Application", f"A victory plaque on the wall listing successful real-world deployments and boundary verifications.", "Conclusion / QED"),
            ],
            examiner_recall_secret=f"Examiners award full marks when you explicitly draw the labeled framework and verify boundary conditions for {topic}.",
        )

"""
Richard Feynman Technique Intuition & Physical Analogy Engine
============================================================
Explains complex engineering and scientific concepts using intuitive everyday metaphors,
first-principles mental models, and conversational clarity without technical jargon.
"""

from typing import Dict, Any, List
from dataclasses import dataclass


@dataclass
class FeynmanIntuition:
    concept: str
    academic_definition: str
    everyday_physical_analogy: str
    the_10_year_old_explanation: str
    core_mathematical_insight: str
    why_examiners_care: str
    mental_model_anchor: str


FEYNMAN_KNOWLEDGE_BASE = {
    "deadlock": FeynmanIntuition(
        concept="Operating System Deadlock (Coffman Conditions)",
        academic_definition="A state where a set of processes are blocked because each process holds a resource and waits for another resource held by another process in a circular chain.",
        everyday_physical_analogy="Imagine a four-way intersection with four stubborn drivers simultaneously entering from North, South, East, and West. Each driver is blocking the path of the car to their left while demanding that car move first. No one can move forward, no one wants to reverse, and everyone is stuck forever.",
        the_10_year_old_explanation="You and your brother want to build a Lego castle. You have all the blue bricks, and he has all the red bricks. You won't share your blue ones until he gives you the red ones, and he won't share his red ones until you give him the blue ones. So neither of you gets to play, and you both sit on the floor crying.",
        core_mathematical_insight="Deadlock exists if and only if all four Coffman conditions hold: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait. Breaking just ONE condition eliminates deadlocks completely.",
        why_examiners_care="Examiners love asking how to break Coffman conditions. Memorize: Resource ordering graph prevents circular wait; preemption allows snatching resources.",
        mental_model_anchor="Traffic intersection gridlock: break the circle or bring a tow truck.",
    ),
    "paging_and_virtual_memory": FeynmanIntuition(
        concept="Paging & Virtual Memory",
        academic_definition="A memory management scheme by which a computer stores and retrieves data from secondary storage for use in main memory in fixed-size blocks called pages and frames.",
        everyday_physical_analogy="Think of your study desk as RAM (fast, but small) and the giant library bookshelf behind you as your Hard Drive (huge, but slow to walk to). Paging is having an assistant bring only the exact 2 pages of the textbook you are currently reading to your desk. When you flip the page, if it's not on the desk, that's a 'Page Fault'—your assistant walks to the bookshelf, fetches the new page, and swaps it in.",
        the_10_year_old_explanation="Your brain can only hold three thoughts at once. When you need to remember your grandmother's recipe, your brain pushes out the cartoon song you were humming to make room. That's swapping!",
        core_mathematical_insight="Virtual Address = Page Number (p) + Offset (d). Physical Address = Frame Number (f) * Page Size + Offset (d). The offset never changes!",
        why_examiners_care="Numerical questions ALWAYS ask to calculate Page Table Size = (2^VirtualBits / PageSize) * EntrySize. Keep page offset bits separate.",
        mental_model_anchor="Study desk vs. Library bookshelf.",
    ),
    "b_tree": FeynmanIntuition(
        concept="B-Tree & B+ Tree Indexing",
        academic_definition="A self-balancing search tree in which each node can contain more than two children, optimized for systems that read and write large blocks of memory on magnetic disks.",
        everyday_physical_analogy="A binary search tree is like a dictionary where you can only ask 'is the word before or after M?'. A B-Tree is like a giant department store directory: you enter the lobby, look at the big board, and in one glance it tells you 'Electronics -> Floor 4, Shoes -> Floor 2, Food -> Floor 1'. With 100 choices per board, you find your item in just 2 or 3 elevators trips instead of taking 20 separate staircases.",
        the_10_year_old_explanation="It's a treasure map with many signposts at every crossroads instead of just two, so you find the treasure in way fewer steps.",
        core_mathematical_insight="High fan-out (M children per node) minimizes disk I/O seek time because tree height scales as O(log_M N) rather than O(log_2 N).",
        why_examiners_care="Why B+ trees over B-trees in databases? B+ trees keep all data pointers in leaf nodes linked sequentially, making range queries (SELECT * WHERE age BETWEEN 20 AND 30) a simple pointer scan without revisiting root.",
        mental_model_anchor="Department store directory with express elevators.",
    ),
}


class FeynmanAnalogizer:
    """
    Pedagogical Explainer converting abstract math & engineering into intuitive mental models.
    """

    def explain(self, concept_query: str) -> FeynmanIntuition:
        lower_query = concept_query.lower()

        # Look up concept
        for key, intuition in FEYNMAN_KNOWLEDGE_BASE.items():
            if any(term in lower_query for term in key.split("_")):
                return intuition

        # Fallback dynamic synthesis
        return FeynmanIntuition(
            concept=concept_query.title(),
            academic_definition=f"Formal engineering abstraction and mathematical model governing {concept_query}.",
            everyday_physical_analogy=f"Imagine a busy post office sorting packages. Instead of handling every letter one by one with a dedicated courier, {concept_query} sets up organized sorting bins with standardized conveyor belts so that thousands of parcels move smoothly without collisions.",
            the_10_year_old_explanation=f"It's like organizing your toy box with labeled compartments so you can find your favorite superhero in two seconds instead of dumping all your toys on the rug.",
            core_mathematical_insight="Optimizes energy and time trade-offs by enforcing strict boundary invariants across all operational cycles.",
            why_examiners_care=f"University examiners look for fundamental understanding: always state the governing axioms, draw the labeled block diagram, and verify boundary limits.",
            mental_model_anchor=f"The organized post office conveyor belt.",
        )

"""
Tests for IEEE Paper Engine & Exam Forensics
"""

import os
import unittest
from anna.core.ieee_paper_engine import IEEEPaperEngine
from anna.core.exam_forensics import ExamForensicsEngine
from anna.core.feynman_analogizer import FeynmanAnalogizer
from anna.core.flashcard_generator import FlashcardGenerator


class TestIEEEAndExam(unittest.TestCase):
    def setUp(self):
        self.output_dir = "test_output"
        self.ieee_engine = IEEEPaperEngine(output_dir=self.output_dir)
        self.exam_engine = ExamForensicsEngine()
        self.feynman = FeynmanAnalogizer()
        self.flashcards = FlashcardGenerator(output_dir=self.output_dir)

    def test_ieee_paper_generation(self):
        res = self.ieee_engine.generate_paper("Edge Computing Distributed Consensus")
        self.assertTrue(os.path.exists(res["latex_file"]))
        self.assertTrue(os.path.exists(res["html_file"]))
        with open(res["latex_file"], "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("\\documentclass{article}", content)
        with open(res["html_file"], "r", encoding="utf-8") as f:
            self.assertIn("IEEE Access", f.read())

    def test_exam_readiness_report(self):
        rep = self.exam_engine.generate_exam_readiness_checklist(
            subject_name="Operating Systems",
            total_exam_marks=70,
        )
        self.assertGreater(rep.predicted_success_rate, 40.0)
        self.assertGreaterEqual(len(rep.pareto_80_20_topics), 4)
        self.assertIn("Banker's Safety Condition", rep.last_minute_formula_sheet)

    def test_feynman_mental_model(self):
        fey = self.feynman.explain("Deadlock")
        self.assertIn("intersection", fey.everyday_physical_analogy.lower())
        self.assertIn("Coffman", fey.core_mathematical_insight)

    def test_flashcard_generation(self):
        res = self.flashcards.generate_deck("Algorithms")
        self.assertTrue(os.path.exists(res["csv_file"]))
        self.assertGreaterEqual(res["total_cards"], 2)


if __name__ == "__main__":
    unittest.main()

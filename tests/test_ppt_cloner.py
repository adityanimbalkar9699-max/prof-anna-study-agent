"""
Tests for PPT Cloner and SIH Optimizer
"""

import os
import unittest
from anna.core.ppt_cloner import PPTCloner
from anna.core.sih_optimizer import SIHOptimizer


class TestPPTAndSIH(unittest.TestCase):
    def setUp(self):
        self.output_dir = "test_output"
        self.ppt_cloner = PPTCloner(output_dir=self.output_dir)
        self.sih_optimizer = SIHOptimizer()

    def test_sih_optimizer(self):
        sample_slides = [
            {"title": "Intro", "bullets": ["We do everything with AI", "It is disruptive"]},
        ]
        res = self.sih_optimizer.analyze_and_optimize(
            sample_slides,
            ps_id="SIH-2024-PS1482",
            project_title="Edge Diagnostic Mesh",
        )
        self.assertGreaterEqual(res.overall_sih_readiness_score, 0)
        self.assertEqual(len(res.optimized_slides_schema), 7)
        self.assertGreater(len(res.jury_defense_cheat_sheet), 0)

    def test_ppt_cloner_export(self):
        schema = [
            {"is_title": True, "category": "HACKATHON DEFENSE", "title": "Test Title", "subtitle": "Test Subtitle"},
            {"is_title": False, "section": "ARCHITECTURE", "title": "System Topology", "cards": [{"heading": "Nodes", "bullets": ["Alpha", "Beta"]}]},
        ]
        out = self.ppt_cloner.clone_and_replace(schema, {"title": "Test Title", "author": "Aditya"}, output_filename="test_deck.pptx")
        self.assertTrue(os.path.exists(out["pptx_file"]))
        self.assertTrue(os.path.exists(out["html5_file"]))
        self.assertGreater(os.path.getsize(out["pptx_file"]), 1000)


if __name__ == "__main__":
    unittest.main()

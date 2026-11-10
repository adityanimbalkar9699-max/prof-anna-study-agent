"""
Unit Tests for Omni-Disciplinary Solver, Universal Diagrams, Video Scripts & Memory Palace
"""

import os
import unittest
from anna.core.omni_solver import OmniDisciplinarySolver
from anna.core.omni_diagrams import OmniDiagramStudio
from anna.core.video_script_engine import VideoScriptEngine
from anna.core.memory_palace import MemoryPalaceStudio


class TestOmniEngines(unittest.TestCase):
    def setUp(self):
        self.output_dir = "test_output_omni"
        self.solver = OmniDisciplinarySolver()
        self.diagrams = OmniDiagramStudio(output_dir=self.output_dir)
        self.video_engine = VideoScriptEngine(output_dir=self.output_dir)
        self.memory_palace = MemoryPalaceStudio()

    def test_omni_solver_upsc_8marks(self):
        ans = self.solver.solve("Examine the doctrine of Separation of Powers under Indian Constitution", target_marks=8)
        self.assertEqual(ans.target_marks, 8)
        self.assertEqual(ans.field_domain, "UPSC_CIVIL_SERVICES")
        self.assertIn("Kesavananda", ans.governing_statute_or_theory)
        self.assertGreaterEqual(len(ans.core_working_or_provisions), 2)
        self.assertIn("Way Forward", ans.conclusion_way_forward)

    def test_omni_solver_commerce_ca(self):
        ans = self.solver.solve("Explain the Fundamental Accounting Equation and double-entry rules", target_marks=10)
        self.assertEqual(ans.field_domain, "COMMERCE_ACCOUNTING")
        self.assertIn("Assets = Capital + Liabilities", ans.governing_statute_or_theory)
        self.assertIsNotNone(ans.step_calculations)

    def test_omni_solver_medical_neet(self):
        ans = self.solver.solve("Explain the countercurrent mechanism in nephron for urine concentration", target_marks=8)
        self.assertEqual(ans.field_domain, "MEDICAL_NEET")
        self.assertIn("Henle", ans.examiner_trap_warning)
        self.assertIn("Guyton", ans.governing_statute_or_theory)

    def test_omni_solver_jee_sciences(self):
        ans = self.solver.solve("Analyze the Carnot engine efficiency and state the 4 stages", target_marks=5)
        self.assertEqual(ans.field_domain, "JEE_PHYSICAL_SCIENCES")
        self.assertEqual(ans.target_marks, 5)

    def test_omni_diagram_action_potential(self):
        res = self.diagrams.render_diagram("Neuronal Action Potential", filename_prefix="test_ap")
        self.assertTrue(os.path.exists(res["png_file"]))
        self.assertIn("wikipedia.org", res["fallback_info"]["primary_url"])

    def test_omni_diagram_breakeven(self):
        res = self.diagrams.render_diagram("Cost Volume Profit Breakeven Chart", filename_prefix="test_bep")
        self.assertTrue(os.path.exists(res["png_file"]))

    def test_omni_diagram_polity_svg(self):
        res = self.diagrams.render_diagram("Separation of Powers Triad", filename_prefix="test_polity")
        self.assertTrue(os.path.exists(res["svg_file"]))

    def test_video_script_package(self):
        pkg = self.video_engine.generate_video_package("Transformer Attention Mechanism")
        self.assertTrue(os.path.exists(pkg.script_markdown_path))
        self.assertTrue(os.path.exists(pkg.interactive_html5_deck_path))
        self.assertEqual(len(pkg.scenes), 5)

    def test_memory_palace_schedules(self):
        pkg = self.memory_palace.construct("12 Schedules of Indian Constitution")
        self.assertEqual(pkg.phonetic_acronym, "TEARS OF OLD PM")
        self.assertGreaterEqual(len(pkg.memory_palace_rooms), 2)
        self.assertIn("Territory", pkg.breakdown["T"])


if __name__ == "__main__":
    unittest.main()

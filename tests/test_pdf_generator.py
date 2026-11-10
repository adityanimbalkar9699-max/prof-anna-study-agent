"""
Tests for PDF Generator & Diagram Engine
"""

import os
import unittest
from anna.core.assignment_solver import AssignmentSolver
from anna.core.pdf_generator import AcademicPDFGenerator
from anna.core.diagram_engine import DiagramEngine


class TestPDFAndDiagram(unittest.TestCase):
    def setUp(self):
        self.output_dir = "test_output"
        self.pdf_engine = AcademicPDFGenerator(output_dir=self.output_dir)
        self.diagram_engine = DiagramEngine(output_dir=self.output_dir)
        self.solver = AssignmentSolver()

    def test_diagram_generation_and_fallback(self):
        res = self.diagram_engine.generate_diagram("Transformer Multi-Head Attention", diagram_type="architecture", filename_prefix="test_diag")
        self.assertTrue(os.path.exists(res["svg_file"]))
        self.assertIn("arxiv.org", res["fallback_info"]["primary_url"])

    def test_matplotlib_chart_generation(self):
        res = self.diagram_engine.generate_diagram("Algorithm Benchmarks", diagram_type="benchmark_chart", filename_prefix="test_chart")
        self.assertTrue(os.path.exists(res["png_file"]))

    def test_pdf_generation(self):
        sol = self.solver.solve("Solve recurrence T(n) = 2T(n/2) + n")
        diag = self.diagram_engine.generate_diagram("Algorithm Benchmarks", diagram_type="benchmark_chart", filename_prefix="chart_for_pdf")
        pdf_path = self.pdf_engine.generate_assignment_pdf(
            solution_data=sol.to_dict(),
            filename="test_solution.pdf",
            diagram_image_path=diag["png_file"],
        )
        self.assertTrue(os.path.exists(pdf_path))
        self.assertGreater(os.path.getsize(pdf_path), 1000)


if __name__ == "__main__":
    unittest.main()

"""
Full End-to-End Integration Test for Prof. Anna Sovereign Agent
"""

import os
import unittest
from anna.core.professor import ProfAnna


class TestFullIntegration(unittest.TestCase):
    def setUp(self):
        self.output_dir = "integration_test_output"
        self.anna = ProfAnna(base_output_dir=self.output_dir)

    def test_complete_study_workflow(self):
        # 1. Assignment solve
        problem = "Solve recurrence T(n) = 2T(n/2) + n for undergraduate algorithms"
        solution = self.anna.solve_assignment(problem, total_marks=10)
        self.assertIsNotNone(solution.final_answer)

        # 2. Check solution
        audit = self.anna.check_solution(problem, solution.final_answer, total_marks=10.0)
        self.assertIsNotNone(audit.overall_score)

        # 3. Diagram generation with fallback
        diag = self.anna.generate_diagram("Transformer Multi-Head Attention", diagram_type="architecture")
        self.assertTrue(os.path.exists(diag["svg_file"]))

        # 4. Anti-AI PDF generation
        pdf_path = self.anna.generate_pdf(
            solution_data=solution.to_dict(),
            filename="integration_verified_report.pdf",
            audit_data=audit.to_dict(),
            diagram_image_path=diag["png_file"],
        )
        self.assertTrue(os.path.exists(pdf_path))

        # 5. PPT and SIH Optimization
        sih_res = self.anna.optimize_sih_deck(
            [{"title": "Overview", "bullets": ["AI system"]}],
            ps_id="SIH-1024",
            project_title="Water Grid Sensor",
        )
        ppt_out = self.anna.clone_presentation(
            sih_res.optimized_slides_schema,
            {"title": "Water Grid Sensor", "author": "Aditya"},
            output_filename="integration_deck.pptx",
        )
        self.assertTrue(os.path.exists(ppt_out["pptx_file"]))

        # 6. IEEE Access Paper
        paper = self.anna.generate_ieee_paper("Edge Distributed Computing")
        self.assertTrue(os.path.exists(paper["latex_file"]))

        # 7. Exam Forensics
        exam_report = self.anna.analyze_exam_readiness(subject_name="Operating Systems")
        self.assertGreater(exam_report.predicted_success_rate, 0)

        # 8. Feynman Analogy & Flashcards
        fey = self.anna.explain_feynman("Paging and Virtual Memory")
        self.assertIn("study desk", fey.everyday_physical_analogy.lower())

        cards = self.anna.generate_flashcards("Operating Systems")
        self.assertTrue(os.path.exists(cards["csv_file"]))


if __name__ == "__main__":
    unittest.main()

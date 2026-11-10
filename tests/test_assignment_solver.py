"""
Tests for Assignment Solver
"""

import unittest
from anna.core.assignment_solver import AssignmentSolver


class TestAssignmentSolver(unittest.TestCase):
    def setUp(self):
        self.solver = AssignmentSolver()

    def test_solve_recurrence(self):
        sol = self.solver.solve("Solve recurrence T(n) = 2T(n/2) + O(n)")
        self.assertIn("Theta(n \\log n)", sol.final_answer)
        self.assertEqual(len(sol.derivation_steps), 4)
        self.assertEqual(sol.confidence_score, 1.0)
        self.assertIn("base_case", sol.formal_proof)

    def test_solve_os_deadlock(self):
        sol = self.solver.solve("Find safe state using Banker's Algorithm for processes P0-P4")
        self.assertIn("SAFE STATE", sol.final_answer)
        self.assertGreaterEqual(len(sol.derivation_steps), 3)

    def test_solve_dbms_normalization(self):
        sol = self.solver.solve("Normalize relation R(A, B, C, D, E) with functional dependencies")
        self.assertIn("Lossless", sol.final_answer)

    def test_to_dict_serializable(self):
        sol = self.solver.solve("Solve eigenvalue problem for 2x2 matrix")
        d = sol.to_dict()
        self.assertEqual(d["assignment_id"], "MTH-EIG-005")
        self.assertIn("derivation_steps", d)


if __name__ == "__main__":
    unittest.main()

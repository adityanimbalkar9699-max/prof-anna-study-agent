"""
Tests for Solution Checker ("City & Cheque")
"""

import unittest
from anna.core.solution_checker import SolutionChecker


class TestSolutionChecker(unittest.TestCase):
    def setUp(self):
        self.checker = SolutionChecker()

    def test_audit_good_solution(self):
        prob = "Solve recurrence relation T(n) = 2T(n/2) + n"
        sol = """Given T(n) = 2T(n/2) + n, with base case T(1) = 1.
Parameters: a = 2, b = 2, f(n) = n.
By Master Theorem, p = log2(2) = 1.
f(n) = Theta(n^1), satisfying Case 2.
Boundary check: For n=1, T(1) = 1 holds.
Therefore, final answer is T(n) = Theta(n log n). Q.E.D."""
        audit = self.checker.audit_solution(prob, sol, total_marks=10.0)
        self.assertGreaterEqual(audit.percentage, 80.0)
        self.assertTrue(audit.boundary_cases_covered)
        self.assertTrue(audit.is_exam_ready)

    def test_audit_flawed_solution(self):
        prob = "Solve recurrence relation T(n) = 2T(n/2) + n"
        sol = "It is n log n"
        audit = self.checker.audit_solution(prob, sol, total_marks=10.0)
        self.assertLess(audit.percentage, 75.0)
        self.assertFalse(audit.boundary_cases_covered)
        self.assertFalse(audit.is_exam_ready)
        self.assertGreater(len(audit.detected_traps_or_fallacies), 0)


if __name__ == "__main__":
    unittest.main()

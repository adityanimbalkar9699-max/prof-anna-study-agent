"""
Master Test Runner for Prof. Anna Sovereign Agent
=================================================
Executes all unit and integration test suites, validating 100% exit code 0.
"""

import sys
import os
import unittest

# Ensure project root is in PYTHONPATH
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


def run_all():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=os.path.join(PROJECT_ROOT, "tests"), pattern="test_*.py")
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    print(f"Total Tests Run: {result.testsRun}")
    print(f"Failures:       {len(result.failures)}")
    print(f"Errors:         {len(result.errors)}")
    print("=" * 60)
    
    if result.wasSuccessful():
        print("[SUCCESS] 100% EMPIRICAL VERIFICATION PASSED: ALL ENGINES OPERATING WITH EXIT CODE 0")
        sys.exit(0)
    else:
        print("[FAIL] VERIFICATION FAILED")
        sys.exit(1)


if __name__ == "__main__":
    run_all()

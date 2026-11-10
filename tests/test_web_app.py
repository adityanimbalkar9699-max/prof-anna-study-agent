"""
Unit Tests for Flask Web Application & REST API
"""

import json
import unittest
from app import app


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_health_check(self):
        res = self.client.get("/health")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["status"], "healthy")
        self.assertEqual(data["mode"], "all-rounder")

    def test_index_dashboard(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Prof. Anna", res.data)

    def test_api_omni_solve(self):
        payload = {
            "question": "Examine Separation of Powers under Indian Constitution",
            "marks": 8,
            "domain": "UPSC_CIVIL_SERVICES"
        }
        res = self.client.post("/api/omni-solve", data=json.dumps(payload), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["field_domain"], "UPSC_CIVIL_SERVICES")
        self.assertIn("Kesavananda", data["governing_statute_or_theory"])

    def test_api_diagram(self):
        payload = {"topic": "Nephron"}
        res = self.client.post("/api/diagram", data=json.dumps(payload), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn("fallback_info", data)

    def test_api_pdf_generation(self):
        payload = {"topic": "Master Theorem Complexity", "marks": 10, "subject": "DAA"}
        res = self.client.post("/api/pdf", data=json.dumps(payload), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data["success"])
        self.assertIn("download_url", data)

    def test_api_video_script(self):
        payload = {"topic": "Transformer Attention"}
        res = self.client.post("/api/video-script", data=json.dumps(payload), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertGreaterEqual(len(data["scenes"]), 5)

    def test_api_mnemonic(self):
        payload = {"topic": "12 Schedules"}
        res = self.client.post("/api/mnemonic", data=json.dumps(payload), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn("TEARS", data["acronym"])


if __name__ == "__main__":
    unittest.main()

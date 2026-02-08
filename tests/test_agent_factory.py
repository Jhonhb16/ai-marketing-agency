import unittest
from escale_ai.agent_factory import AgentFactory


class TestAgentFactory(unittest.TestCase):
    def test_base_pipeline(self):
        result = AgentFactory.run_base_pipeline()
        self.assertIsInstance(result, dict)
        expected_keys = [
            "supervisor",
            "prospector",
            "outreach",
            "appointment_setter",
            "proposal_builder",
            "qa_compliance",
        ]
        for key in expected_keys:
            self.assertIn(key, result)

    def test_client_pipeline(self):
        result = AgentFactory.run_client_pipeline("Test Clinic")
        self.assertIsInstance(result, dict)
        expected_keys = [
            "account_manager",
            "growth_strategist",
            "funnel_architect",
            "creative_director",
            "media_buyer",
            "qa_compliance_ads",
        ]
        for key in expected_keys:
            self.assertIn(key, result)


if __name__ == "__main__":
    unittest.main()

import unittest

from automation_engines import EventBridge, Trigger


class EventBridgeTests(unittest.TestCase):
    def test_executes_read_safe_action(self):
        decision = EventBridge().route(Trigger("dashboard", "report", 1, {}))

        self.assertEqual(decision.route, "execute")
        self.assertTrue(decision.dry_run)

    def test_holds_low_clearance_write_action(self):
        decision = EventBridge().route(Trigger("operator", "deploy", 2, {}))

        self.assertEqual(decision.route, "hold")

    def test_reviews_high_clearance_write_action(self):
        decision = EventBridge().route(Trigger("operator", "deploy", 5, {}))

        self.assertEqual(decision.route, "review")

    def test_rejects_bad_tier(self):
        decision = EventBridge().route(Trigger("operator", "report", 9, {}))

        self.assertEqual(decision.route, "reject")


if __name__ == "__main__":
    unittest.main()


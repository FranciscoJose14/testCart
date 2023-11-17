import unittest
from main.main import analyze_feedback

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        feedback_list = [
            "The service was excellent! Highly recommended.",
            "I had a terrible experience with the product quality.",
            "Good customer support and quick resolution.",
            "Very bad customer support and slow attention.",
            "Poor packaging and delivery service."
        ]
        expected_output = {
            'Most Frequent Positive Words': ['excellent', 'highly', 'recommended', 'good', 'quick'],
            'Most Frequent Negative Words': ['terrible', 'bad', 'slow', 'poor'],
            'Overall Sentiment Score': 1,
            'Sentiment Report': 'Positive to Negative Ratio = 1.25:1'
        }
        self.assertEqual(analyze_feedback(feedback_list), expected_output)

    def test_case_2(self):
        feedback_list = [
            "This is a good product.",
            "Excellent service!",
            "Satisfied with my purchase."
        ]
        expected_output = {
            'Most Frequent Positive Words': ['good', 'excellent'],
            'Most Frequent Negative Words': [],
            'Overall Sentiment Score': 3,
            'Sentiment Report': 'Positive to Negative Ratio = N/A'
        }
        self.assertEqual(analyze_feedback(feedback_list), expected_output)

    def test_case_3(self):
        feedback_list = [
            "The service was bad.",
            "Poor customer experience.",
            "Terrible quality product."
        ]
        expected_output = {
             'Most Frequent Positive Words': [],
             'Most Frequent Negative Words': ['bad', 'poor', 'terrible'],
             'Overall Sentiment Score': -3,
             'Sentiment Report': 'Positive to Negative Ratio = 0.00:1'
        }
        self.assertEqual(analyze_feedback(feedback_list), expected_output)

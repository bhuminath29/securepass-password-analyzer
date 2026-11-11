import unittest

from analyzer import analyze_password


class TestPasswordAnalyzer(unittest.TestCase):

    def test_empty_password(self):
        result = analyze_password("")

        self.assertEqual(result["strength"], "Very Weak")

    def test_common_password(self):
        result = analyze_password("password")

        self.assertTrue(result["common"])
        self.assertEqual(result["strength"], "Very Weak")

    def test_repeated_characters(self):
        result = analyze_password("aaaa1111")

        self.assertTrue(result["repeated"])

    def test_sequential_password(self):
        result = analyze_password("123456")

        self.assertTrue(result["sequence"])

    def test_strong_example(self):
        result = analyze_password("Maple!Orbit82#River")

        self.assertEqual(result["strength"], "Very Strong")

    def test_password_length(self):
        result = analyze_password("Hello123!")

        self.assertEqual(result["length"], 9)


if __name__ == "__main__":
    unittest.main()
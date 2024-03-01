import os
import sys

# Add the src directory to sys.path to find the executor module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join(parent_dir, 'src')
sys.path.insert(0, src_dir)


import unittest
from io import StringIO
from contextlib import redirect_stdout

from executor import execute_rogue_script

class TestRogueLang(unittest.TestCase):
    def test_rogue_files(self):
        test_files_dir = os.path.join(os.path.dirname(__file__), 'test_files')
        answer_files_dir = os.path.join(os.path.dirname(__file__), 'answer_files')
        failures = []

        for test_file in os.listdir(test_files_dir):
            if test_file.endswith('.rogue'):
                with open(os.path.join(test_files_dir, test_file), 'r') as file:
                    test_input = file.read()
                with open(os.path.join(answer_files_dir, test_file.replace('.rogue', '_expected.txt')), 'r') as file:
                    expected_output = file.read().strip()

                actual_output = StringIO()
                with redirect_stdout(actual_output):
                    execute_rogue_script(os.path.join(test_files_dir, test_file))
                actual_output = actual_output.getvalue().strip()

                if actual_output != expected_output:
                    failures.append((test_file, test_input, expected_output, actual_output))

        # Report the test results
        if failures:
            print(f"Failed {len(failures)} tests.")
            for name, test_input, expected, actual in failures:
                print(f"\nTest: {name}\nInput:\n{test_input}\nExpected:\n{expected}\nActual:\n{actual}")
        else:
            print("All tests passed.")

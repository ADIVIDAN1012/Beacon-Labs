import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

import tests.test_parser_keywords as tp

def run_tests():
    print("Running tests from test_parser_keywords.py...")
    failures = 0
    tests_run = 0
    
    # Simple test discovery
    for name in dir(tp):
        if name.startswith('test_'):
            func = getattr(tp, name)
            if callable(func):
                print(f"Running {name}...", end=' ')
                try:
                    func()
                    print("PASS")
                except Exception as e:
                    print(f"FAIL: {e}")
                    failures += 1
                tests_run += 1
    
    print(f"\nRan {tests_run} tests.")
    if failures == 0:
        print("All tests passed!")
        sys.exit(0)
    else:
        print(f"{failures} tests failed.")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()

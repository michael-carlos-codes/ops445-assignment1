#!/usr/bin/env python3
# Student ID: Michael Carlos

import subprocess
import sys

def run_test(command, expected_output, expected_exit_code=0):
    """Run the test by executing a command and comparing its output with the expected output."""
    print(f"Running test: {' '.join(command)}")

    # Run the command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Check exit code
    if result.returncode != expected_exit_code:
        print(f"Error: Expected exit code {expected_exit_code}, but got {result.returncode}")
        print(f"Output: {result.stdout}")
        print(f"Error: {result.stderr}")
        sys.exit(1)
    
    # Check if output matches expected output
    if result.stdout.strip() == expected_output.strip():
        print(f"Test passed!")
    else:
        print(f"Test failed!")
        print(f"Expected: {expected_output}")
        print(f"Actual: {result.stdout.strip()}")
        sys.exit(1)

def test_valid_date_range():
    """Test a valid date range"""
    command = ['python3', 'assignment1.py', '2023-05-01', '2023-05-30']
    expected_output = "The period between 2023-05-01 and 2023-05-30 includes 8 weekend days."
    run_test(command, expected_output)

def test_reversed_date_range():
    """Test a reversed date range"""
    command = ['python3', 'assignment1.py', '2023-05-30', '2023-05-01']
    expected_output = "The period between 2023-05-30 and 2023-05-01 includes 8 weekend days."
    run_test(command, expected_output)

def test_invalid_date():
    """Test invalid date input"""
    command = ['python3', 'assignment1.py', '2023-02-31', '2023-05-30']
    expected_output = "Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD"
    run_test(command, expected_output, expected_exit_code=1)

def test_missing_argument():
    """Test missing argument"""
    command = ['python3', 'assignment1.py', '2023-05-01']
    expected_output = "Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD"
    run_test(command, expected_output, expected_exit_code=1)

def test_valid_date_with_custom_dates():
    """Test with a valid custom date range for milestone 2"""
    command = ['python3', 'assignment1.py', '2024-03-01', '2024-03-15']
    expected_output = "The period between 2024-03-01 and 2024-03-15 includes 4 weekend days."
    run_test(command, expected_output)

def main():
    """Run all the tests"""
    print("Starting tests...\n")
    
    # Run all the individual tests
    test_valid_date_range()
    test_reversed_date_range()
    test_invalid_date()
    test_missing_argument()
    test_valid_date_with_custom_dates()  # Add milestone 2 test
    
    print("\nAll tests passed!")

if __name__ == '__main__':
    main()

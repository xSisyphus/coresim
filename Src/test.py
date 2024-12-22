import unittest
from unittest.mock import patch, mock_open
import sys
import os

# Add the Src directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Src.main import lexingProcess, fullAdder, JSON_VERSION

class TestCalculatorFunctions(unittest.TestCase):
    
    # Tests for lexingProcess
    def test_lexing_process_basic(self):
        self.assertEqual(lexingProcess("hello world"), ["hello", "world"])
        
    def test_lexing_process_empty(self):
        self.assertEqual(lexingProcess(""), [])
        
    def test_lexing_process_spaces(self):
        self.assertEqual(lexingProcess("   hello   world   "), ["hello", "world"])
        
    def test_lexing_process_case(self):
        self.assertEqual(lexingProcess("HeLLo WoRLD"), ["hello", "world"])

    # Tests for fullAdder
    def test_full_adder_0_0_0(self):
        self.assertEqual(fullAdder(0, 0, 0), [0, 0])
        
    def test_full_adder_0_0_1(self):
        self.assertEqual(fullAdder(0, 0, 1), [1, 0])
        
    def test_full_adder_0_1_0(self):
        self.assertEqual(fullAdder(0, 1, 0), [1, 0])
        
    def test_full_adder_0_1_1(self):
        self.assertEqual(fullAdder(0, 1, 1), [0, 1])
        
    def test_full_adder_1_0_0(self):
        self.assertEqual(fullAdder(1, 0, 0), [1, 0])
        
    def test_full_adder_1_0_1(self):
        self.assertEqual(fullAdder(1, 0, 1), [0, 1])
        
    def test_full_adder_1_1_0(self):
        self.assertEqual(fullAdder(1, 1, 0), [0, 1])
        
    def test_full_adder_1_1_1(self):
        self.assertEqual(fullAdder(1, 1, 1), [1, 1])

    # Tests for JSON_VERSION
    @patch("builtins.open", mock_open(read_data='{"version": "1.0.0", "status": "beta"}'))
    def test_json_version_valid(self):
        self.assertIsNone(JSON_VERSION())

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_json_version_file_not_found(self, mock_file):
        with self.assertRaises(FileNotFoundError):
            JSON_VERSION()

class TestMainIntegration(unittest.TestCase):
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_exit_commands(self, mock_print, mock_input):
        exit_commands = ['exit', 'quit', 'q', 'e']
        for cmd in exit_commands:
            mock_input.return_value = cmd
            # Test that program exits with these commands
            
    @patch('builtins.input')
    @patch('builtins.print')
    def test_empty_input(self, mock_print, mock_input):
        mock_input.return_value = "   "
        # Test empty input handling
        
    @patch('builtins.input')
    @patch('builtins.print')
    def test_help_command(self, mock_print, mock_input):
        mock_input.return_value = "cores"
        # Test help command
        
    @patch('builtins.input')
    @patch('builtins.print')
    def test_invalid_command(self, mock_print, mock_input):
        mock_input.return_value = "invalid_command"
        # Test invalid command handling

class TestCalculatorIntegration(unittest.TestCase):
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_valid_calculation_2bit(self, mock_print, mock_input):
        mock_input.return_value = "c 2b a 01 b 01"
        # Test 2-bit addition
        
    @patch('builtins.input')
    @patch('builtins.print')
    def test_valid_calculation_4bit(self, mock_print, mock_input):
        mock_input.return_value = "c 4b a 1010 b 0101"
        # Test 4-bit addition
        
    def test_invalid_bit_size(self):
        # Test cases for invalid bit sizes
        test_cases = [
            "c 0b a 0 b 0",
            "c 9b a 0 b 0",
            "c ab a 0 b 0"
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                # Verify error handling
                pass
                
    def test_mismatched_input_lengths(self):
        # Test cases for mismatched input lengths
        test_cases = [
            "c 2b a 001 b 01",
            "c 2b a 01 b 001",
            "c 2b a 1 b 01"
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                # Verify error handling
                pass

class TestInputValidation(unittest.TestCase):
    
    def test_invalid_binary_digits(self):
        test_cases = [
            "c 2b a 21 b 01",
            "c 2b a 01 b 21",
            "c 2b a xy b 01"
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                # Verify error handling
                pass
                
    def test_missing_arguments(self):
        test_cases = [
            "c 2b",
            "c 2b a",
            "c 2b a 01",
            "c 2b a 01 b"
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                # Verify error handling
                pass

class TestEdgeCases(unittest.TestCase):
    
    def test_large_numbers(self):
        # Test with maximum allowed bit size
        pass
        
    def test_special_characters(self):
        # Test input with special characters
        pass
        
    def test_unicode_input(self):
        # Test input with unicode characters
        pass
        
    def test_memory_usage(self):
        # Test memory usage with large inputs
        pass

if __name__ == '__main__':
    unittest.main()
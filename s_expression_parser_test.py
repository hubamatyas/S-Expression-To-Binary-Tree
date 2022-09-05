"""
Run with: pytest s_expression_parser_test.py
Open cov_tests/s_expression_parser.html for coverage test report
"""

from s_expression_parser import ParseToBinaryTree

def test_get_answer():
    testParser = ParseToBinaryTree('1(1()())')
    assert 'no' == testParser.get_answer()

def test_clean_s_expression():
    testParser = ParseToBinaryTree('1(1(0)(0))')
    cleaned_s_expression = testParser.clean_s_expression('1(1(0)(0))')
    assert cleaned_s_expression == ['1', '1', '0', '0']

def test_clean_s_expression_complex():
    testParser = ParseToBinaryTree('20(5(4(11(7()())(2()()))())(8(13()())(4()(1()()))))')
    cleaned_s_expression = testParser.clean_s_expression('20(5(4(11(7()())(2()()))())(8(13()())(4()(1()()))))')
    assert cleaned_s_expression == ['20', '5', '4', '11', '7', 'null', 'null', '2', 'null', 'null', 'null', '8', 
                                    '13', 'null', 'null', '4', 'null', '1', 'null', 'null']
    
def test_build_binary_tree_with_empty_tree():
    testParser = ParseToBinaryTree('1()')
    testParser.build_binary_tree()
    answer = testParser.get_answer()
    assert answer == 'no'

def test_build_binary_tree_with_correct_root_to_path_sum():
    testParser = ParseToBinaryTree('1(1(0)(0))')
    testParser.build_binary_tree()
    answer = testParser.get_answer()
    assert answer == 'yes'

def test_build_binary_tree_with_complex_and_correct_root_to_path_sum():
    testParser = ParseToBinaryTree('22(5(4(11(7()())(2()()))())(8(13()())(4()(1()()))))')
    testParser.build_binary_tree()
    answer = testParser.get_answer()
    assert answer == 'yes'

def test_build_binary_tree_with_incorrect_root_to_path_sum():
    testParser = ParseToBinaryTree('1(1(1)(1))')
    testParser.build_binary_tree()
    answer = testParser.get_answer()
    assert answer == 'no'

def test_build_binary_tree_with_complex_and_incorrect_root_to_path_sum():
    testParser = ParseToBinaryTree('20(5(4(11(7()())(2()()))())(8(13()())(4()(1()()))))')
    testParser.build_binary_tree()
    answer = testParser.get_answer()
    assert answer == 'no'


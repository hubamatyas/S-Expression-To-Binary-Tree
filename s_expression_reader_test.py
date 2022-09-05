"""
Run with: pytest s_expression_reader_test.py
Open cov_tests/s_expression_reader.html for coverage test report
"""

from s_expression_reader import ReadTestFile

def test_get_s_expressions():
    testReader = ReadTestFile('')
    assert testReader.get_s_expressions() == []

def test_empty_file():
    testReader = ReadTestFile('test_files/test_empty_file.txt')
    testReader.read_file()
    assert len(testReader.get_s_expressions()) == 0

def test_empty_expression():
    testReader = ReadTestFile('test_files/test_empty_expression.txt')
    testReader.read_file()
    assert len(testReader.get_s_expressions()) == 1

def test_file_with_invalid_char():
    testReader = ReadTestFile('test_files/test_file_with_invalid_char.txt')
    try:
        testReader.read_file()
    except ValueError as e:
        assert len(testReader.get_s_expressions()) == 0
        assert e.args[0] == 'Invalid character in input'

def test_one_expression():
    testReader = ReadTestFile('test_files/test_one_expression.txt')
    testReader.read_file()
    expression = testReader.get_s_expressions()
    assert len(expression) == 1
    assert expression[0] == '22(5(4(11(7()())(2()()))())(8(13()())(4()(1()()))))'

def test_one_expression_with_spaces():
    testReader = ReadTestFile('test_files/test_one_expression_with_spaces.txt')
    testReader.read_file()
    expression = testReader.get_s_expressions()
    assert len(expression) == 1
    assert expression[0] == '22(5(4(11(7()())(2()()))())(8(13()())(4()(1()()))))'

def test_one_expression_with_newlines():
    testReader = ReadTestFile('test_files/test_one_expression_with_newlines.txt')
    testReader.read_file()
    expression = testReader.get_s_expressions()
    assert len(expression) == 1
    assert expression[0] == '22(5(4(11(7()())(2()()))())(8(13()())(4()(1()()))))'

def test_multiple_expressions():
    testReader = ReadTestFile('test_files/test_multiple_expressions.txt')
    testReader.read_file()
    expression = testReader.get_s_expressions()
    assert len(expression) == 2
    assert expression == ['22(5(4(11(7()())(2()()))())(8(13()())(4()(1()()))))', 
                        '20(5(4(11(7()())(2()()))())(8(13()())(4()(1()()))))']

def test_multiple_expressions_with_spaces():
    testReader = ReadTestFile('test_files/test_multiple_expressions_with_spaces.txt')
    testReader.read_file()
    expression = testReader.get_s_expressions()
    assert len(expression) == 2
    assert expression == ['22(5(4(11(7()())(2()()))())(8(13()())(4()(1()()))))', 
                        '20(5(4(11(7()())(2()()))())(8(13()())(4()(1()()))))']

def test_multiple_expressions_with_newlines():
    testReader = ReadTestFile('test_files/test_multiple_expressions_with_newlines.txt')
    testReader.read_file()
    expression = testReader.get_s_expressions()
    assert len(expression) == 4
    assert expression == ['22(5(4(11(7()())(2()()))())(8(13()())(4()(1()()))))', 
                        '20(5(4(11(7()())(2()()))())(8(13()())(4()(1()()))))',
                        '10(3(2(4()())(8()()))(1(6()())(4()())))',
                        '5()']



from s_expression_reader import ReadTestFile
from s_expression_parser import ParseToBinaryTree

def main():
    reader = ReadTestFile('sample_input.txt')
    try:
        reader.read_file()
    except ValueError as e:
        print('Error:', e.args[0])
        return

    for s_expression in reader.get_s_expressions():
        parser = ParseToBinaryTree(s_expression)
        parser.build_binary_tree()
        answer = parser.get_answer()
        print(answer)

if __name__ == "__main__":
    main()
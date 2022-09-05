class ReadTestFile():
    def __init__(self, file_name):
        self.file_name = file_name
        self.nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        """
        If '-' is added to the allowed chars the program can also correctly
        calculate the sums of root-to-leaf paths with negative integers.
        """
        self.allowed_chars = ['(', ')']
        self.skippable_chars = [' ', '', '\n']
        self.s_expressions = []

    def get_s_expressions(self):
        return self.s_expressions

    def read_file(self):
        with open(self.file_name, 'rt') as file:
            # read and store first char to be able check for end of S expression
            first_char = file.read(1)
            s_expression = first_char
            previous_char = first_char

            for line in file:
                for char in line:
                    """
                    Skip spaces, new lines and any other char that's not part of a valid
                    S expression as described in the brief
                    """
                    if char in self.allowed_chars or char in self.nums:
                        """
                        If it wasn't a known fact that all S expression are valid in the
                        test file, validity should be checked here with the use of a stack
                        """
                        if char in self.nums and previous_char == ')':
                            self.s_expressions.append(s_expression)
                            s_expression = ''

                        s_expression += char
                        previous_char = char
                    elif char not in self.skippable_chars:
                        self.s_expressions = []
                        raise ValueError('Invalid character in input')

            # handle empty file
            if s_expression != '':
                # append last S expression that ended with end-of-file
                self.s_expressions.append(s_expression)
            
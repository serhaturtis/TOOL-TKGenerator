class CodeGenerator:
    
    def __init__(self, indentation='    '):
        self.indentation=indentation
        self.current_level = 0
        self.code = ''

    def indent(self):
        self.current_level += 1

    def dedent(self):
        if self.current_level > 0:
            self.current_level -= 1

    def line(self, value):
        self.code = self.code + ''.join([self.indentation for i in range(0, self.current_level)]) + str(value) + '\n'

    def get_code(self):
        return self.code

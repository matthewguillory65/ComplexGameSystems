class Parser(object):
    def __init__(self, expression):
        self.expression = expression

def main():
    parser = Parser('(A + B) * (B + C)')
    print parser.expression

main()
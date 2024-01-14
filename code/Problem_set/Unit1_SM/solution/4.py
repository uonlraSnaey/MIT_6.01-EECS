class CommentsSM(sm.SM):
    start_state = "NORMAL"

    def getNextValues(self, state, inp):
        if state == "NORMAL":
            if inp == '#':
                return ("INSIDE_COMMENT", inp)
            elif inp == "'":
                return ("INSIDE_STRING", inp)
            else:
                return ("NORMAL", None)
        elif state == "INSIDE_COMMENT":
            if inp == '\n':
                return ("NORMAL", None)
            else:
                return ("INSIDE_COMMENT", inp)
        elif state == "INSIDE_STRING":
            if inp == "'":
                return ("NORMAL", None)
            else:
                return ("INSIDE_STRING", inp)

# Example usage:
program_str = '''def f(x): # comment
return 1'''

m = CommentsSM()
output = m.transduce(program_str)

print(output)

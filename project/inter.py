
def opening(filename):
    f = open(filename, "r")
    run(f.read())
    f.close()
    

def parse(code):
    return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))


def body(code):
    opened = []
    bodies = {}
    for i in range(len(code)):
        if code[i] == '[':
            opened.append(i)
        elif code[i] == ']':
            bodies[i] = opened[-1]
            bodies[opened.pop()] = i
    return bodies

def run(code):
    code = parse(code)
    bodies = body(code)
    x = i = 0
    bf = {0:0}
    while i < len(code):
        sym = code[i]
        if sym == '>':
            x += 1
            bf.setdefault(x, 0)
        elif sym == '<':
            x -= 1
        elif sym == '+':
            bf[x] += 1
        elif sym == '-':
            bf[x] -= 1
        elif sym == '.':
            print(chr(bf[x]), end='')
        elif sym == ',':
            bf[x] = int(input('Input: '))
        elif sym == '[':
            if not bf[x]: i = bodies[i]
        elif sym == ']':
            if bf[x]: i = bodies[i]
        i += 1
        

opening('brainfuck.txt')






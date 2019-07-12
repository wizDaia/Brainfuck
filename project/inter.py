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
        
def main():
    input_value = '0'
    while (input_value < '4'):
        input_value = input('======Brainfuck interprete====== \n Choose your fighter: \n 1.Code from .txt \n 2.Code from input \n 3.Exit \n')
        if input_value == '1':
            print('Result: ')
            opening("brainfuck.txt")
        elif input_value == '2':
            code = input('Enter your code in one line: \n')
            print('Result: ')
            run(code)             
        elif input_value == '3':
            exit(0)
        

if __name__ == "__main__": main()





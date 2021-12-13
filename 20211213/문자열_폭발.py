import sys
input = sys.stdin.readline

def main():

    string = str(input().strip('\n'))
    bomb = str(input().strip('\n'))

    stack = []
    last = bomb[-1] 


    for char in string:
        stack.append(char)
        #마지막 글자가 일치하는 경우 
        #스택에서 글자수만큼 비교 후 맞으면 지우기
        if char == last and ''.join(stack[-len(bomb):]) == bomb:
            del stack[-len(bomb):]

    answer = ''.join(stack)
    if answer:
        print(answer)
    else:
        print('FRULA')

if __name__ == '__main__':
    main()
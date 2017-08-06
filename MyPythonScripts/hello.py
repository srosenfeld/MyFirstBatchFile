#! python3

import sys
print('Hello world')
name = ''

if len(sys.argv) > 1:
    name = sys.argv[1]
    print('Hello %s' %(name))
    print('Here are the arguments:\n')
    print(sys.argv)

    print('What would you like to learn about?')
    answer = input()
    print("OK %s, let me think about that. \n I don't know if I would have said '%s', but I always heard '%s likes it that way!'" % (name, answer, name))

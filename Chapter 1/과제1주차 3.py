import queue

a = input("문자열을 입력해라")
stack  = queue.LifoQueue(maxsize=20)
for c in a:
    stack.put(c)

for i in range(stack.qsize()):
    print(stack.get(),end="")

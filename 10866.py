import sys

def push_front(x):
    deque.insert(0, x)

def push_back(x):
    deque.append(x)

def pop_front():
    if len(deque) == 0:
        return -1
    else:
        return deque.pop(0)

def pop_back():
    if len(deque) == 0:
        return -1
    else:
        return deque.pop()

def size():
    return len(deque)

def empty():
    if len(deque) == 0:
        return 1
    else:
        return 0

def front():
    if len(deque) == 0:
        return -1
    else:
        return deque[0]

def back():
    if len(deque) == 0:
        return -1
    else:
        return deque[-1]


N = int(sys.stdin.readline().rstrip())
deque = []

for _ in range(N):
    S = sys.stdin.readline().rstrip().split()

    order = S[0]
    if order == "push_front":
        push_front(S[1])
    elif order == "push_back":
        push_back(S[1])
    elif order == "pop_front":
        print(pop_front())
    elif order == "pop_back":
        print(pop_back())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "front":
        print(front())
    elif order == "back":
        print(back())
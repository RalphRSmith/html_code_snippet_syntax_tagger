from collections import deque

class D_Stack:
    def __init__(self):
        self.stack = deque()
        self.size = 0

    def push(self, x):
        '''inserts an item onto the stack'''
        self.stack.append(x)
        self.size += 1

    def pop(self):
        '''returns the last item added to the stack'''
        if self.size > 0:
            self.size -= 1
            return self.stack.pop()

    def top(self):
        '''returns the last inserted value'''
        if self.size > 0:
            return self.stack[-1]

    def __len__(self):
        '''returns the number of items in the stack'''
        return self.size

    def __repr__(self):
        return repr(self.stack)


def test_one():
    '''Test if items come out in Last-In-First-Out order'''
    print("test 1: ", end="")
    s = D_Stack()
    s.push(1)
    s.push(5)
    try:
        assert(s.pop() == 5)
        assert(s.pop() == 1)
        print("passed")
    except assertionError:
        print("failed")


def test_two():
    '''Test if len returns the correct size'''
    print("test 2: ", end="")
    s = D_Stack()
    s.push(1)
    s.push(5)
    s.push(3)
    s.pop()
    try:
        assert(len(s) == 2)
        print("passed")
    except assertionError:
        print("failed")


def test_three():
    '''Make sure that trying to pop an empty stack terminates'''
    print("test 3: ", end="")
    s = D_Stack()
    for i in range(5):
        s.push(i)

    try:
        while s:
            s.pop()
        print("passed")
    except error as e:
        print("failed")
        raise e


def test_four():
    '''Make sure top returns the value of the last element inserted into the stack'''
    print("test 4: ", end="")
    s = D_Stack()
    for i in range(5):
        s.push(i)

    s.push(99)

    try:
        assert(s.top() == 99)
        print("passed")
    except assertionError:
        print("failed")


def main():
    test_one()
    test_two()
    test_three()
    test_four()


if __name__ == "__main__":
    main()

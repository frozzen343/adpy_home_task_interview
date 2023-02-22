"""Task 1."""

class Stack():
    def __init__(self) -> None:
        self.data = str()

    def is_empty(self) -> bool:
        """Check stack for empty."""
        return not bool(self.data)
    
    def push(self, element: str) -> None:
        """Add a new element to stack."""
        self.data += element

    def pop(self) -> str:
        """Delete last element in stack.
        Return last element.
        """
        self.data = self.data[:-1]
        if not self.is_empty():
            return self.data[-1]

    def peek(self) -> str:
        """Return last element in stack."""
        return self.data[-1]
    
    def size(self) -> int:
        """Return elements count in stack."""
        return len(self.data)


"""Task 2."""

def main() -> str:
    stack = Stack()
    stack.data = '(((([{}]))))'

    brackets = {
        '(': 0,
        ')': 0,
        '[': 0,
        ']': 0,
        '{': 0,
        '}': 0,
    }

    brackets[stack.peek()] += 1
    
    while stack.size()-1:
        brackets[stack.pop()] += 1

    if brackets['('] == brackets[')'] and \
        brackets['['] == brackets[']'] and \
        brackets['{'] == brackets['}']:
        return print('Сбалансированно') 
    else:
        return print('Несбалансированно') 


if __name__ == '__main__':
    main()
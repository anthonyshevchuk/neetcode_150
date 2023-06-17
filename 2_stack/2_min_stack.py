# https://leetcode.com/problems/min-stack/
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.mins.append(val)

        else:
            self.mins.append(min(val, self.mins[-1]))

        self.stack.append(val)

    def pop(self) -> None:
        self.mins.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1] if self.stack else None


if __name__ == '__main__':
    min_stack = MinStack()
    for num in [-2, 0, -1]:
        min_stack.push(num)
    print(min_stack.getMin())  # -2
    print(min_stack.top())  # -1
    min_stack.pop()
    print(min_stack.getMin())  # -2

class Stack:
  # initialize an empty list
  def __init__(self):
      self.items = []
  # push a new item to the last index
  def push(self, item):
      self.items.append(item)
  # remove the last item
  def pop(self):
      # if the stack is empty, return None
      # (it would also be reasonable to throw an exception)
      if not self.items:
          return None
      return self.items.pop()
  # see what the last item is
  def peek(self):
      if not self.items:
          return None
      return self.items[-1]

# push -> update largest at time of push
# pop -> when I pop, change back to largest at time of push
class MaxStack:
  # initialize an empty list
  def __init__(self):
      self.stack = Stack()
      self.largest = None
  # push a new item to the last index
  def push(self, item):
      if item > self.largest:
        self.stack.push(self.largest)
        self.stack.push(item)
        self.largest = item
    else:
        self.stack.push(item)

  # remove the last item
  def pop(self):
      item = self.stack.pop()
      if item < self.largest:
        return item
    else:
        self.largest = self.stack.pop()

  def peek(self):
      return self.stack.peek()

stk = MaxStack()
stk.push(1)
x = stk.peek()
print(x)
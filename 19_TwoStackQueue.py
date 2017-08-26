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


class Queue:
    def __init__(self):
        self.left = Stack()
        self.right = Stack()
    
    def enqueue(self, item):
        self.right.push(item)

    def dequeue(self):
        if self.left.peek() is None:
            while self.right.peek() is not None:
                item = self.right.pop()
                self.left.push(item)
            if self.left.peek() is None:
                raise IndexError('Queue is empty')
        item = self.left.pop()
        return item
        
q = Queue()

for i in range(5):
    q.enqueue(i)

x = q.dequeue()
print(x)

# while x:
#     print(x)
#     x = q.dequeue()


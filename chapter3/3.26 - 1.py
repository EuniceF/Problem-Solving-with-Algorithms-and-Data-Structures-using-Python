class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)
    # pop: return the stack top and delete the top
	def pop(self):
		return self.items.pop()
	# peek: return the stack top
	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)

# function defination
def toBinary(num):
	binstack = Stack()
	while num > 0:
		binstack.push(num%2)
		num = num // 2
	binstring = ""
	while not binstack.isEmpty():
		binstring += str(binstack.pop())
	return binstring

print(toBinary(17))
print(toBinary(45))
print(toBinary(96))

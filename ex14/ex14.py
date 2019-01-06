class DLLNode(object):
    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        return f"{self.prev} <- {self.value} -> {self.next}"

class DLList(object):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def push(self, obj):
        pass

    def pop(self):
        pass
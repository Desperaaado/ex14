class DLLNode(object):
    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        # return f"{self.prev} <- {self.value} -> {self.next}"
        return f"=={self.value}=="

class DLList(object):
    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        if not self.begin:
            self.begin = DLLNode(obj, None, None)
            self.end = self.begin
        elif self.begin == self.end:
            node = DLLNode(obj, None, self.begin)
            self.end = node
            self.begin.next = node
        else:
            node = self.end
            node.next = DLLNode(obj, None, self.end)
            self.end = node.next

    def pop(self):
        if not self.begin:
            print('Empty List!')
            result = None
        elif self.begin == self.end:
            result = self.begin.value
            self.begin = None
            self.end = None
        else:
            result = self.end.value
            node = self.end.prev
            node.next = None
            self.end = node

        return result
        
    def dump(self, mode='normal'):
        the_list = []

        if mode == 'normal':
            node = self.begin
            
            if not node:
                print('Empty List!')
                return None

            the_list.append(node.value)

            while node.next:
                node = node.next
                the_list.append(node.value)

        print('list: ', the_list)
        return the_list

    def remove(self, obj):
        pass
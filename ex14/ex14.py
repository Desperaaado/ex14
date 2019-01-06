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
        node = self.begin

        if mode == 'silence':
            silence = True
        else:
            silence = False
        
        if not node:
            if not silence:
                print('Empty List!')
            return None

        the_list.append(node.value)

        while node.next:
            node = node.next
            the_list.append(node.value)

        if not silence:
            print('list: ', the_list)

        return the_list

    def remove(self, obj):
        the_list = self.dump('silence')
        if not(obj in the_list):
            print('Not in the list!')
            return None

        if self.begin == self.end:
            self.begin = None
            self.end = None
            result = 0
        else:
            result = 0
            node = self.begin
            
            while node.value != obj:
                result += 1
                node = node.next
            
            if node.next:
                node.next.prev = node.prev
            node.prev.next = node.next

        return result

    def first(self):
        return self.begin and self.begin.value or None

    def last(self):
        return self.end and self.end.value or None

    def get(self, index):
        the_list = self.dump('silence')
        
        if index > len(the_list) - 1:
            print('Out of range!')
            return None
        else:
            return the_list[index]

    def count(self):
        the_list = self.dump('silence')
        return len(the_list)

    def shift(self, obj):
        if not self.begin:
            self.begin = self.end = DLLNode(obj, None, None)
        elif self.begin == self.end:
            node = DLLNode(obj, self.end, None)
            self.end.prev = node
            self.begin = node
        else:
            node = DLLNode(obj, self.begin, None)
            self.begin.prev = node
            self.begin = node

    def unshift(self):
        if not self.begin:
            print('Empty List!')
            result = None
        elif self.begin == self.end:
            result = self.begin.value
            self.begin = self.end = None
        else:
            result = self.begin.value
            node = self.begin.next
            node.prev = None
            self.begin = node

        return result

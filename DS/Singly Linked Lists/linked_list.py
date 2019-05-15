from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
    
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node isn't in the list")
            return
        
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def find_node(self, data):
        current_node = self.head
        while current_node.data != data:
            current_node = current_node.next
        return current_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def delete_node_pos(self, pos):
        current_node = self.head
        if pos == 0:
            if current_node:
                self.head = current_node.next
                current_node = None
                return
        i = 0
        while i < pos:
            if current_node.next:
                current_node = current_node.next
                i += 1
            else:
                return "There's no data in that position"
        self.delete_node(current_node.data)

    def swap(self, k1, k2):
        if k1 == k2:
            return

        node_1 = self.find_node(k1)
        node_2 = self.find_node(k2)
        
        before_k1 = None
        before_k2 = None

        prev_node = None
        current_node = self.head
        while current_node and current_node.data != k1:
            prev_node = current_node
            current_node = current_node.next
        before_k1 = prev_node

        prev_node = None
        current_node = self.head
        while current_node and current_node.data != k2:
            prev_node = current_node
            current_node = current_node.next
        before_k2 = prev_node

        if before_k1:
            before_k1.next = node_2
        else:
            self.head = node_2
        if before_k2:
            before_k2.next = node_1
        else:
            self.head = node_1

        node_1.next, node_2.next = node_2.next, node_1.next

    def len_iterative(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def reverse_iterative(self):
        current_node = self.head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def reverse_recursive(self):

        def _reverse_recursive(current_node, prev_node):
            if not current_node:
                return prev_node
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, prev_node)

        self.head = _reverse_recursive(self.head, None)
        
    def merge_sorted(self, llist):
        
        first_list = self.head
        second_list = llist.head
        merged_list = None

        if not first_list:
            return second_list
        if not second_list:
            return first_list

        if first_list and second_list:
            if first_list.data <= second_list.data:
                merged_list = first_list
                first_list = merged_list.next
            else:
                merged_list = second_list
                second_list = merged_list.next
            new_head = merged_list
        while first_list and second_list:
            if first_list.data <= second_list.data:
                merged_list.next = first_list
                merged_list = first_list
                first_list = merged_list.next
            else:    
                merged_list.next = second_list
                merged_list = second_list
                second_list = merged_list.next
        if not first_list:
            merged_list.next = second_list
        if not second_list:
            merged_list.next = first_list

        self.head = new_head
        llist.head = None
        return new_head

    def remove_duplicate(self):
        current_node = self.head
        prev_node = None
        duplicates = dict()
        
        while current_node:
            if current_node.data in duplicates:
                prev_node.next = current_node.next
                current_node = None
            else:
                duplicates[current_node.data] = 1
                prev_node = current_node
            current_node = prev_node.next

    def print_nth_from_last(self, n):
        # Method 1

        # total_len = self.len_iterative()
        # current_node = self.head
        # while current_node:
        #     if total_len == n:
        #         print(current_node.data)
        #         return current_node
        #     total_len -= 1
        #     current_node = current_node.next
        # if current_node is None:
        #     return

        # Method 2

        p = self.head
        q = self.head
        
        counter = 0
        while q and counter < n:
            q = q.next
            counter += 1
        if not q:
            print(str(n) + "is greater than the number of nodes in list.")
            return
        while p and q:
            p = p.next
            q = q.next
        return p.data

    def count_occurences_iterative(self, data):
        current_node = self.head
        count = 0
        while current_node:
            if current_node.data == data:
                count += 1
            current_node = current_node.next
        if count == 0:
            return ("There wasn't any node with data = " + str(data))
        return count

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)    
    
    def rotate(self, key):
        p = self.head
        q = self.head
        
        count = 1 
        while p and count < key:
            p = p.next
            count += 1
        count = 1
        while q and count < key:
            q = q.next
            count +=1
        while q.next:
            q = q.next
        last_node = p
        p = p.next
        q.next = self.head
        self.head = p
        last_node.next = None
    
    def is_palindrome(self):
        text = ""
        current_node = self.head
        while current_node:
            text += current_node.data
            current_node = current_node.next
        return text == text[::-1]
    
    def move_tail_to_head(self):
        current_node = self.head
        prev_node = None

        while current_node.next:
            prev_node = current_node
            current_node = current_node.next
        current_node.next = self.head
        prev_node.next = None
        self.head = current_node
        
    def sum_two_lists(self, first_list, second_list):
        lfl = first_list.len_iterative()
        lsl = second_list.len_iterative()
        first_list = first_list.head
        second_list = second_list.head
        first_value = 0
        second_value = 0
        for i in range(lfl):
            first_value += first_list.data * ( 10 ** (lfl - i - 1))
            first_list = first_list.next
        for i in range(lsl):
            second_value += second_list.data * ( 10 ** (lsl - i - 1))
            second_list = second_list.next
        
        return first_value + second_value

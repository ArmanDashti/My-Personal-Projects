from node import Node
from linked_list import LinkedList

l = LinkedList()
l.append("A")
l.append("B")
l.append("C")
l.append("D")

l.print_list()
l.move_tail_to_head()
print('\n')
l.print_list()
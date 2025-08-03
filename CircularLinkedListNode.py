class CircularLinkedListNode:
    def __init__ (self, head, value, tail):
        self.head = head
        self.value = value
        self.tail = tail
        
class CircularLinkedList:
    def __init__ (self, nodes, initial):
        self.nodes = nodes
        self.initial = initial
        
    def find_node_by_head(self, head):
        for node in self.nodes:
            if node.head == head:
                return node
        return None
    
    def print_list(self):
        isInitial = True
        print_node = self.initial

        while (isInitial):
            print(f"Head: {print_node.head}, Value: {print_node.value}, Tail: {print_node.tail}")
            print_node = self.find_node_by_head(print_node.tail)
            
            if print_node.head == self.initial.head:
                isInitial = False

node_1 = CircularLinkedListNode("002", "データA", "222")
node_2 = CircularLinkedListNode("222", "データB", "501")
node_3 = CircularLinkedListNode("501", "データC", "700")
node_4 = CircularLinkedListNode("700", "データE", "224")
node_5 = CircularLinkedListNode("224", "データE", "002")

myLinkedList = CircularLinkedList([node_1, node_2, node_3, node_4, node_5], node_1)
myLinkedList.print_list()
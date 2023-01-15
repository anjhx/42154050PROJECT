from no_element import NoElement
import time

class ListNode:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

class LinkedList:
    """A singly linked list."""

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size
    def append(self, new_data):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = ListNode(new_data)
        self._size=self._size+1
        # 4. If the Linked List is empty, then make the
        # new node as head
        if self._head is None:
            self._head = new_node
        else:
            # 5. Else traverse till the last node
            last = self._head
            while (last.next):
                last = last.next

            # 6. Change the next of last node
            last.next = new_node
    def index_of(self, key):
            idx = -1       
            walk = self._head
            while walk is not None:
                
                idx += 1
                if walk.key == key:
                    return idx
                else:
                    walk = walk.next
            raise IndexError
        
    #i是1开示 
    def get_node(self, i) -> ListNode:
        if i < 1 or i > self._size+1:
            raise IndexError('Out of bounds')
        else:
            cnt = 1
            walk = self._head
            while cnt < i:
                walk = walk.next
                cnt = cnt + 1
            return walk

    def get(self, i):
        walk = self.get_node(i)
        assert walk is not None
        return walk.key

    def remove(self):
        self._size = self._size-1
        if self._head == None:
            raise IndexError('Remove from empty linked list')
        if self._head.next == None:
            self._head = None
        else: 
            second_last = self._head
            while(second_last.next.next):
                second_last = second_last.next
            second_last.next = None
            
        

    def swap(self, n1, n2):  
        prevNode1 = None  
        prevNode2 = None
        node1 = self._head
        node2 = self._head
          
        #Checks if list is empty  
        if(self._head == None):  
            raise NoElement
              
        #If n1 and n2 are equal, then list will remain the same  
        if(n1 == n2):  
            raise IndexError 
              
        #Search for node1  
        while(node1 != None and node1.key != n1):  
            prevNode1 = node1 
            node1 = node1.next
              
        #Search for node2  
        while(node2 != None and node2.key != n2):  
            prevNode2 = node2
            node2 = node2.next
              
        if(node1 != None and node2 != None):  
              
            #If previous node to node1 is not None then, it will point to node2  
            if(prevNode1 != None):  
                prevNode1.next = node2
            else:  
                self._head  = node2 
                  
            #If previous node to node2 is not None then, it will point to node1  
            if(prevNode2 != None):  
                prevNode2.next = node1
            else:  
                self._head  = node1
                  
            #Swaps the next nodes of node1 and node2  
            temp = node1.next
            node1.next = node2.next
            node2.next = temp
        else:  
            print("Swapping is not possible")






#if __name__ == '__main__':
        #ll = LinkedList()
        #ll.append(4)
        #ll.append(3)
        #ll.swap(4,3)
        #print(ll._head.key)
        #print(ll.get(2))


class MinPQ:
    """A min binary heap."""
 

    def __init__(self):
        self.ll = LinkedList()

    def size(self):
        return self.ll.size()

    def is_empty(self):
        return self.size() == 0

    def _swap(self, i, j):
        m = self.ll.get_node(i)
        n = self.ll.get_node(j)
        self.ll.swap(m.key,n.key)
    def _more(self, i, j):
        a = self.ll.get_node(i)
        b = self.ll.get_node(j)
        return a.key > b.key

    def _swim(self, k):
        while k > 1 and self._more(k//2, k):
            self._swap(k//2, k)
            k//= 2 

    def _sink(self, k):
        while 2 * k <= self.size():
            j = 2 * k
            if j < self.size() and self._more(j, j + 1):
                j += 1
            if not self._more(k, j):
                break
            self._swap(k, j)
            k = j

    def insert(self, key): 
        self.ll.append(key)
        self._swim(self.size())
   

    def min(self):
        if self.is_empty():
            raise NoElement
        return self.ll.get(1)

    def del_min(self):
        if self.is_empty():
            raise NoElement
        root = self.ll._head
        self._swap(1, self.size())
        self.ll.remove()
        self._sink(1)
        return root

    def _is_min_heap_ordered(self, k):
        if k > self.size():
            return True
        left = 2 * k
        right = 2 * k + 1
        if left <= self.size() and self._more(k, left):
            return False
        if right <= self.size() and self._more(k, right):
            return False
        return self._is_min_heap_ordered(left) and self._is_min_heap_ordered(right)

    def _is_min_heap(self):
        if self.ll._head is None:
            return False
        return self._is_min_heap_ordered(1)

if __name__ == '__main__':
    pq  = MinPQ()

    for i in reversed(range (1,20)):
        start_time = time.time()
        pq.insert(i)
        end_time = time.time()
        t = end_time-start_time
        print ('%d.cost %f OF INSERT' %(i+1,t))
    for i in range(1,19):
        start_time = time.time()
        pq.del_min()
        end_time = time.time()
        t = end_time-start_time
        print ('%d.cost %f OF delmin' %(i+1,t))


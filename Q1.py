from collections import deque
 
 
# A Binary Tree Node
class BtreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

 
# A Linked List Node
class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
 
def datalist(listnode):
    res = []
    head = listnode
    temp = head
    while temp:
        res.append(temp.data)
        temp = temp.next
    return res
def leftchild(ll,idx):
    return ll[2*(idx+1)-1]
def rightchild(ll,idx):   
    return(ll[2*(idx+1)])
def parent(ll,idx):
    return(ll[idx//2])
# Function to perform preorder traversal on a given binary tree.
def preorder(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right) 
# Function to construct a complete binary tree from a given linked list
class convert:
    def __init__(self) -> None:
       self.size = 0 
    def converse2tree(head):
        # base case
        if head is None:
            return None
    
        # create the root using the first node of the linked list
        root =BtreeNode(head.data)
        convert().size +1

        # move the head pointer to the next node
        head = head.next
    
        # create a queue to store tree pointers and enqueue the root node
        q = deque()
        q.append(root)
    
        # loop till the end of the linked list is reached
        while head:
            # dequeue front node
            front = q.popleft()
    
            # create a left child from the next node in the linked list and enqueue it
            front.left = BtreeNode(head.data)
            convert().size +1
            q.append(front.left)
    
            # move the head pointer to the next node
            head = head.next
    
            # if the linked list did not reach its end
            if head:
                # create the right child from the next node in the linked list and
                # enqueue it
                front.right = BtreeNode(head.data)
                convert().size +1
                q.append(front.right)
    
                # move the head pointer to the next node
                head = head.next
    
        # return root of the constructed binary tree
        return root
  

    







    

if __name__ == '__main__':

    head = None
    n = 6

    # construct a linked list
    for i in reversed(range(1, n + 1)):
        head = ListNode(i, head)
    ll = datalist(head)
    print(ll)
    root = convert.converse2tree(head)
    print(leftchild(ll,2))
    print('\n')
    preorder(root)

 

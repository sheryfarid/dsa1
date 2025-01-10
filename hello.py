class node:
    # create constructor to pass my value and next to connect to next node
    def __init__(self,value = 0 ,next=None):
        self.value = value 
        self.next = next 
def reverselinklist (head :node):
        # funtion to reverse list using stack 
        if not head :
            # if list is empty , return none
            return None
        #push all nodeinto stack
        stack = []
        current = head 
        while current:
            stack.append(current)
            current = current.next
        # now pop all node to build reverse list
        newhead = stack.pop()
        current = newhead
        while stack:
            current.next = stack.pop()
            current = current.next 
        # set next node of last node as none 
        current.next = None
        return newhead
def printlinklist(head:node):
        # function to traverse and print link list 
        while head:
            print(head.value,end="- >")
            head = head.next 
        print("None")


head = node(1, node(2, node(3, node(4,None)))) # create head as a object to pass node with their vslue 
printlinklist(head) # to print original list
reversehead = reverselinklist(head) 
printlinklist(reversehead) # then pass reverse list

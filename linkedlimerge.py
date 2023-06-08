#You will be given two linked lists, each of whose nodes is represented by the following structure--

# The function takes two pointers 'list1' and 'list2', each of them polnang to the stare of a linked list. Both the lists represent two non-negative numbers. Each of their nodes contains a singl digit. Implement the function to add the two numbers and return it as a ticked ist..
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def addTwoNumbers(list1, list2):
    dummy = Node()  # Create a dummy node to serve as the head of the result list
    curr = dummy
    carry = 0

    while list1 or list2 or carry:
        sum_val = carry

        if list1:
            sum_val += list1.value
            list1 = list1.next

        if list2:
            sum_val += list2.value
            list2 = list2.next

        carry = sum_val // 10
        curr.next = Node(sum_val % 10)
        curr = curr.next

    return dummy.next


# Test example
# list1: 2 -> 4 -> 3
# list2: 5 -> 6 -> 4
# Result: 7 -> 0 -> 8

# Create list1
list1 = Node(2)
list1.next = Node(4)
list1.next.next = Node(3)

# Create list2
list2 = Node(5)
list2.next = Node(6)
list2.next.next = Node(4)

# Call the function
result = addTwoNumbers(list1, list2)

# Print the result
while result:
    print(result.value, end=" -> ")
    result = result.next
print("None")

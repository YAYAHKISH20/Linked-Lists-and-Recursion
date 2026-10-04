from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # TODO: 1) Create a LinkedList instance
    from linked_list import LinkedList
 
if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations
    like insertion, recursion-based sum, search, and reverse.
    """
 
    # 1) Create a LinkedList instance
    ll = LinkedList()
 
    # 2) Insert some sample data using insert_at_front or insert_at_end
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_front(5)
 
    # 3) Display the list to verify insertion
    print("Original list:")
    ll.display()
 
    # 4) Call recursive_sum and print the result
    print(f"Sum of all IDs: {ll.recursive_sum()}")
 
    # 5) Call recursive_search with a target and print result
    for target in (20, 99):
        found = ll.recursive_search(target)
        print(f"Is ID {target} in the list? {'Yes' if found else 'No'}")
 
    # 6) Call recursive_reverse, then display the reversed list
    ll.recursive_reverse()
    print("Reversed list:")
    ll.display()

    # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
    
    # TODO: 3) Display the list to verify insertion
    

    # TODO: 4) Call recursive_sum and print the result
    

    # TODO: 5) Call recursive_search with a target and print result
    

    # TODO: 6) Call recursive_reverse, then display the reversed list
    


# 

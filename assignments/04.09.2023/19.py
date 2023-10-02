count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        check = count - n - 1
        count = 0
        curr = head

        # Removing the first node
        if check == -1:  
            return head.next

        while curr:
            if count == check:
                curr.next = curr.next.next
                # As the removal is done, Exit the loop
                break  
            curr = curr.next
            count += 1

        return head
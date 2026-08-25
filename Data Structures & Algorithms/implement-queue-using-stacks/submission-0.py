class MyQueue:
    """
    reverse of stack using queue

    - do in O(1) time

    Queue: pop the earliest element inserted

    bruteforce [1,2,3]
    - push: O(1)
        append to back of stack
    - pop: O(n)
        - movepop all element from stack into stack2 and stop at the last item
        - pop this last element in stack -> the return value
        - movepop back all elemnts in stack2 back to stack
    - peek: O(n)
        same as pop but just don't pop the last element
    - empty: O(1)
    
    Optimal ammortised O(1)
    idea: one of the stack2 maintains instant pop -> right side is the oldest element
        - if you transfer one by one from stack1 to stack2 -> stack2 becomes a 'reversed' queue
        where the earliest element is on the right. stack1 MUST be emptied
        - make sure to never insert new elements into non-empty stack2 as insert should be from the front to be in order
        - pop finish the elements in stack2 and it is empty then you can empty out stack1 again
    - push:
        - push to stack
    - pop:
        - pop stack2 if not empty
        - if stack2 empty, EMPTY stack1 into stack2 then pop stack2
    - peek:
        - peeek stack2 if not empty
        - if stack2 empty, EMPTY stack1 into stack2 then peek top of stack2
    - empty:
        - check both s1 and s2

    you could technically empty out s1 into s2 anytime, even at the push
    mistake: 
    - you can't just insert directly into s2 as s2 is reversed order and rightmost is oldest
    - you must wait for s2 to be empty then you can pop s1 items in. Because 
    - you have to empty out s1 into s2. If you leave behind elements in s1

    [1,2,3,4,5]
    eg. s1, s2
    [1,2], []
    [], [2,1] -> 1 is the item to pop from queue
    [3,4] [2,1]
    - you can't pop 5 into [2,1] as the order is wrong -> need everything in s2 to pop out
    [3,4] []
    [3] [4] -> this is now WRONG, as s1->s2 transfer is a full transfer, can't incremental transfer
    - when s1 -> s2 the newest element is on the left
    - new writes have to go to the left which can't be done, so need to wait for s2 to empty
    - if you don't fully empty s1 to s2, the earliest element is stuck in s1 and not in the top to pop in s2
        - pop is wrong, not the smallest (this is the wrong part)
    - but the next step still gives in ordered answer
    [3,5] []
    [] [5,3]


    Time:
    pop does not empty into s2 everytime. it empties a total of n elements across all iterations n1 + n2 + ... = n
    """

    def __init__(self):
        self.s1 = [] # insert stack
        self.s2 = [] # pop stack
        

    def push(self, x: int) -> None:
        self.s1.append(x)

    
    def pop(self) -> int:
        if not self.s2: # if s2 empty
            # empty s1 into s2
            while self.s1:
                top = self.s1.pop()
                self.s2.append(top)
        return self.s2.pop()
        

    def peek(self) -> int:
        if not self.s2:   
            while self.s1:
                top = self.s1.pop()
                self.s2.append(top)
        return self.s2[-1]
        

    def empty(self) -> bool:
        return bool(not self.s1 and not self.s2)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
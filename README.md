1.  First step was to fix the error by importing the Optional class.
2.  Second step includes, creating the object of class Calendar and
    calling the calendar.book function.
3.  Third step included checking the if-elif condtions which was not
    correctly set.
4.  There were two conditions by which any event can be added to the calendar without double booking,
    a.  After the end of previous event, hence the if condition should
        be changed to node.start \>= self.end, here the new event would
        be added only after the end of previous event.
    b.  Before the start time of next event, hence the elif condition
        should be changed to node.end \<= self.start, so that any new
        event can be added before the next event scheduled.
5.  If the event was added successfully, then it would send the return
    value as true, but if the conditions was not satisfied then the
    return value of the function was sent back as NONE, so there was a
    need to include an else condition where if a event was not added
    then the value should be sent back as "False"

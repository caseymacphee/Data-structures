def merge_sort(numberlist):
    """
Takes a list and sorts it in a first smallest way, doing sorts
in n(log(n))
The function works by breaking the list down to sub lists of 
length 1 and then building back up an ordered list by popping 
the lesser of the two lists to be merged.
    """
    if len(numberlist) < 2:
        return numberlist
    else:
        pivot = len(numberlist) / 2
        leftside = numberlist[:pivot]
        rightside = numberlist[pivot:]
        leftside = merge_sort(leftside)
        rightside = merge_sort(rightside)
        return _merge_sub(leftside, rightside)

def _merge_sub(leftsidelist, rightsidelist):
    combined = []
    while len(leftsidelist) > 0 or len(rightsidelist) > 0:
        if len(leftsidelist) > 0 and len(rightsidelist) > 0:
            ### Now combining the sublists ###
            if leftsidelist[0] <= rightsidelist[0]:
                combined.append(leftsidelist.pop(0))
            else:
                combined.append(rightsidelist.pop(0))
        elif len(leftsidelist) > 0:
            combined.append(leftsidelist.pop(0))
        elif len(rightsidelist) > 0:
            combined.append(rightsidelist.pop(0))
    return combined

if __name__ == '__main__':
    print "ordered list :"
    ordered_list = [1,2,3,4,5]
    print ordered_list
    print merge_sort(ordered_list)
    decending_list = [5,4,3,2,1]
    print "decending ordered list:"
    print decending_list
    print merge_sort(decending_list)
    unordered_list = [4,3,5,3,1,8,2]
    print "unordered list:"
    print unordered_list
    print merge_sort(unordered_list)
    print merge_sort.func_doc

def bubble_sort(lst):
    size = len(lst)-1
    
    for i in range(size):
        for k in range(size-i):
            if lst[k] > lst[k+1]:
                lst[k], lst[k+1] = lst[k+1], lst[k]
    print(lst)
    
    
lst = [6,4,2,1,7,2]

bubble_sort(lst)
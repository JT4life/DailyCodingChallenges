def filter_sort(items):
    lst = []
    for item in items:
        if isinstance(item, str):
            lst.append(item)
    
    return lst.sort()

items = [1,2,'a','c','a']

print(filter_sort(items))
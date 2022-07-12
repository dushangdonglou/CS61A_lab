def insert_items(lst, entry, elem):
    """Inserts elem into lst after each occurence of entry and then returns lst.
    
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    False
    """
    "*** YOUR CODE HERE ***"
    # 方法1 建立new_lst
    # new_lst = []
    # for i in lst:
    #     new_lst.append(i)
    #     if i == entry:
    #         new_lst.append(elem)
    # return new_lst
    # 方法2 在原lst上插入
    # def insert(x, item):
    #     nonlocal lst
    #     lst1 = lst[:x]
    #     lst2 = lst[x:]
    #     lst = lst1 + [item] + lst2
    # i = 0
    # for _ in range(len(lst)):
    #     if lst[i] == entry:
    #         insert(i+1, elem)
    #         i += 1
    #     i += 1
    # return lst

    # 方法3 双指针
    def insert(x, item):
        nonlocal lst
        lst1 = lst[:x]
        lst2 = lst[x:]
        lst = lst1 + [item] + lst2

    left = 0
    right = len(lst) - 1
    while left <= right:
        if left != right:
            if lst[left] == entry:
                insert(left + 1, elem)
                right += 1
                left += 1
            if lst[right] == entry:
                insert(right + 1, elem)
                right -= 1
            left += 1
            right -= 1
        else:
            if lst[left] == entry:
                insert(left + 1, elem)
            break
    return lst



def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


def scale(it, multiplier):
    """Yield elements of the iterable it multiplied by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    for i in it:
        yield i * multiplier

def hailstone(n):
    """Yields the elements of the hailstone sequence starting at n.
    
    # >>> for num in hailstone(10):
    # ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    if n <= 1:
        if n % 2 == 0:
            yield n / 2
        else:
            yield n * 3 + 1
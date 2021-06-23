"""
    [1, 2, 3, 4, 5]
        min 3 => [3, 4, 5]
        max 3 => [1, 2, 3]
        min,max 3 => [3]
    ---------------------------------------------------------------------------
    Sometimes you need to limit array result to use. Such as you only need the
    value over 10 or, you need value under than 100. By use this algorithms, you
    can limit your array to specific value
    If array, Min, Max value was given, it returns array that contains values of
    given array which was larger than Min, and lower than Max. You need to give
    'unlimited' to use only Min or Max.

    ex) limit([1,2,3,4,5], None, 3) = [1,2,3]

    Complexity = O(n)

"""


def limit(arr, min_num=None, max_num=None):
    def min_check(val): return True if min_num is None else (val >= min_num)

    def max_check(val): return True if max_num is None else (val <= max_num)

    return [val for val in arr if min_check(val) and max_check(val)]


print(limit([1, 2, 3, 4, 5]))

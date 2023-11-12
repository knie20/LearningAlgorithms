

from algs.counting import RecordedItem


def is_palindrome(w):
    length = len(w)
    if length < 2:
        return True
    A = [RecordedItem(i) for i in range(length//2)]
    for i in A:
        print('i is ', i)
        if w[i] != w[length-i-1]:
            return False
    return True

print(is_palindrome('abcaaaaasdf'))
print(RecordedItem.report())
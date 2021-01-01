# def rotate_matrix(arr, k):
#     k %= len(arr)
#     reverse(arr, 0, len(arr)-1)
#     reverse(arr, 0, k-1)
#     reverse(arr, k, len(arr)-1)
#     return arr

# def reverse(nums, start, stop):
#     while(start < stop):
#         temp = nums[start]
#         nums[start] = nums[stop]
#         nums[stop] = temp
#         start = start + 1
#         stop = stop-1

# print(rotate_matrix([1,2,3,4], 3))

# def matching_brackets(brackets):
#     Stack = []
#     right_brackets = 0
#     for brac in brackets:
#         if brac == '(':
#             Stack.append(brac)
#         else:
#             right_brackets += 1

#     if len(Stack) == 0:
#         return right_brackets % 2
#     else:
#         for ch in Stack:
#             right_brackets -= 2
#         if right_brackets == 0:
#             return ('Brackets are paired')
#         return abs(right_brackets)

# brackets = '(('
# print(matching_brackets(brackets))


# # class Solution(object):
# #     def addToArrayForm(self, A, K):
# #         array = []

# #         string = ''.join(A)
# #         res = int(string) + K
# #         res = str(res)
# #         for ch in res:
# #             array.append(int(ch))

# # s = Solution()
# # print(s.addToArrayForm([2,1,5], 806))


class EnglishRuler:
    "Drawing an english ruler(in inches)"

    def draw_line(self, tick_length, tick_label=''):
        """Draw one line with given tick length (followed by optional label)"""
        line = '-' * tick_length
        if tick_label:
            line += ' ' + tick_label
        print(line)


    def draw_interval(self, center_length):
        """Draw tick interval based upon a central tick length"""
        if center_length > 0: #stop when length drops to 0
            self.draw_interval(center_length - 1)  # recursively draw top ticks
            self.draw_line(center_length) # draw center ticks
            self.draw_interval(center_length - 1) # recursively draw bottom ticks


    def draw_ruler(self, num_inches, major_length):
        """Draw English ruler with given number of inches, major tick length"""
        self.draw_line(major_length)
        for j in range(1, 1 + num_inches):
            self.draw_interval(major_length - 1)
            self.draw_line(major_length, str(j))

EnglishRuler().draw_ruler(4, 3)


def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a python list.
        The search only considers the portion from data[low] to data[high] inclusive
    """
    if high > len(data):
        raise KeyError("arg value is beyond scope of list")
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # recur on the left side of the list relative to the middle
            return binary_search(data, target, low, mid - 1)
        else:
            # recur on the right side of the list relative to the middle
            return binary_search(data, target, mid +1, high)

if(binary_search([2,4,5,6,7,8,9,10,11,12,13,14,15], 2, 0, 13)):
    print("Found")
else:
    print("Not found")


import os

# total = os.path.getsize('../../Downloads/big bang theory')
def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendants"""
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    return total

print(disk_usage('../../Downloads/big bang theory'))

def fibonacci(n):
    """Return a pair of Fibonacci numbers, F(n) and F(n - 1)"""
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fibonacci(n - 1)
        return (a+b, a)

print(fibonacci(10))

def linear_sum(S, n):
    """Return the sum of the first n numbers of sequence S"""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n-1]

print(linear_sum([1,2,3,4,6,7,32,45,7,8,9], 10))

def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]"""
    if start < stop-1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)

nums = [1,2,3,4,5,6,7,8,9,10,11]
reverse(nums, 0, 10)
print(nums)
        






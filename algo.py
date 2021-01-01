
def deja_vu(str):
    for i in range(0, len(str), 1):
        for j in range(i+1, len(str)):
            if(str[j] == str[i]):
                print("Deja vu at letter", i+1)
                return False
           

deja_vu('banncdefghijklmnopqrstuvwxyza')


result=[]

def compare_arr(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if(arr1[i] == arr2[j]):
                result.append(arr2[j])
    print(result)

compare_arr([1, 2, 3, 4, 5, 6, 7], [6, 7, 3, 5, 9])


result = []
store = []

def compare_arr2(arr1, arr2):
    for i in range(len(arr1)):
        store.append(arr1[i])
    for j in range(len(arr2)):
        if(arr2[j] in store):
            result.append(arr2[j])
    print(result)
    
compare_arr2([1, 2, 3, 4, 5, 6, 7], [6, 7, 3, 4, 9, 5, 5])


def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

nums = [5, 3, 8, 6, 7, 2]
sort(nums)
print(nums)


def bubble_sort(nums):
    nums = [5, 3, 8, 6, 7, 2, 7, 8, 9, 100, 999, 87]
    for i in range(len(nums)-1):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos  = j

        temp = nums[i]
        nums[i]  = nums[minpos]
        nums[minpos] = temp

    print(nums)


bubble_sort(nums)

def search(list, n):
    i = 0

    while i < len(list):
        if list[i] == n:
            return True
        i = i + 1
        
    return False

list = [5, 3, 4, 9, 8]
n = 9

if(search(list, n)):
    print ("Found")
else:
    print("Not found")

def binary_search(arr, n): # list must be sorted
    l = 0 #lower bound
    u = len(arr)-1 #upper bound

    while l <= u:
        mid = (l + u) // 2
        if arr[mid] == n:
            return True
        else:
            if arr[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False
arr = [4, 7, 8, 12, 45, 99]
n = 15

if(binary_search(arr, n)):
    print("Found")
else:
    print("Not found")


# n = input("Enter a number: \n")
# factorial = 1
# if int(n) > 1:
#     for i in range(1, int(n) + 1):
#         factorial = factorial * i
# print(factorial)

def find_factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n < 1:
        return ("NA")
    else:
        return n * find_factorial(n - 1)

print(find_factorial(0))

def find_number(nums, target):
    store = {}
    result = []
    for i, value in enumerate(nums):
        complements = target - value
        store[i] = complements
        if store[i] in nums:
            result.append(i)
    print(result)
find_number([2,11,7,15], 9)

string = input("Enter a sentence: \n")


def avg_word_length(sentence):
    spaces = 0
    num_of_letters = 0

    for ch in sentence:
        if ch == " ":
            spaces = spaces + 1
        else:
            num_of_letters = num_of_letters + 1

    avg_word_length = num_of_letters / (spaces + 1)
    return avg_word_length




print(avg_word_length(string))

def addtodict(nums):
    dict = {}
    count = 0
    for i in range(0, len(nums)):
        dict[i] = nums[i]
    

        

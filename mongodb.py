def isAPerfectSquare(num: int) -> bool:

 
    
    mid = num // 2 # * epic fail
    if mid*mid == num:
        return True
    elif mid*mid > num:
        mid = mid-1




print(isAPerfectSquare(9))


class Solution():
    """
    pascal's triangle(easy)
    """

    def generateRows(self, numRows: int) -> list:
        triangle = []
        if(numRows == 0):
            return triangle

        first_row = [1]
        triangle.append(first_row)

        for i in range(1, numRows):
            prev_row = triangle[i-1]
            row = []
            row.append(1)
            for j in range(1, i):
                row.append(prev_row[j-1] + prev_row[j])

            row.append(1)
            triangle.append(row)
        return triangle


print(Solution().generateRows(3))


def lengthOfLongestSubstring(s: str) -> int:
    if (len(s) == 0):
        return 0
    map = {}
    max_length = start = 0

    for i in range(len(s)):
        if s[i] in map and start <= map[s[i]]:
            start = map[s[i]] + 1
        else:
            max_length = max(max_length, i - start+1)  # - before +
        map[s[i]] = i
    return max_length


print(lengthOfLongestSubstring("abcabc"))

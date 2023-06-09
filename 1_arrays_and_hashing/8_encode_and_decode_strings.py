# https://www.lintcode.com/problem/659/

class Solution1:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        """
        @param: str: A string
        @return: dcodes a single string to a list of strings
        """
        # write your code here
        out = ''
        for i, str_ in enumerate(strs):
            out += str_
            if i < len(strs) - 1:
                if str_ != ':':
                    out += ':;'
                else:
                    out += '::;'
        return out

    def decode(self, str):
        # write your code here
        out = []
        start = 0
        str += ':;'
        for end in range(len(str)):
            if str[end] == ';':
                if str[end - 1] == ':':
                    if str[end - 2] == ':':
                        out.append(str[start: end - 2])
                    else:
                        out.append(str[start:end - 1])

                    start = end + 1

        return out


# another solution
class Solution:
    def encode(self, strs):
        out = ''
        for s in strs:
            out += str(len(s)) + '#' + s
        return out

    def decode(self, str):
        out = []
        start = 0
        while start < len(str):
            j = start
            while str[j] != '#':
                j += 1
            length = int(str[start: j])
            word = str[j + 1: j + 1 + length]
            out.append(word)
            start = j + 1 + length
        return out


if __name__ == '__main__':
    solution = Solution()
    test_case = ["lint", "code"]
    # test_case = ["lint", "code", "love", "you"]
    # test_case = ["we", "say", ":", "yes"]
    # assert solution.decode(solution.encode(test_case)) == test_case
    print(solution.decode(solution.encode(test_case)))
    # print(solution.encode(test_case))

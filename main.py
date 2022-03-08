# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def climbStairs(self, n: int) -> int:
        def path(n, memo=None):
            if memo is None:
                memo = {}
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < 0:
                return
            count = 0
            for i in range(1, 3):
                if path(n - i):
                    count += path(n - i)
            memo[n] = count
            return count
        return path(n)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.climbStairs(4))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

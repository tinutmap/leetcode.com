from .code import MyQueue


def test_1():
    ans = [None]
    a = MyQueue()
    ans.append(a.push(1))
    ans.append(a.push(2))
    ans.append(a.peek())
    ans.append(a.pop())
    ans.append(a.empty())
    res = [None, None, None, 1, 1, False]
    assert ans == res
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


"""
"""

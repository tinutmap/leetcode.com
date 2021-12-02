from .code import MyLinkedList, DoublyListNode


def base(commands, data):
    if data[0] == [] and commands[0] == "MyLinkedList":
        linked_list = MyLinkedList()
        output = [None]
        for i in range(1, min(len(commands), len(data))):
            if data[i] != []:
                val = linked_list.__getattribute__(commands[i])(*data[i])
            if type(val) == type(DoublyListNode()):
                output.append(val.val)
            else:
                output.append(val)
        return output


def test_1():
    commands = ["MyLinkedList", "addAtHead", "addAtTail",
                "addAtIndex", "get", "deleteAtIndex", "get"]
    data = [[], [1], [3], [1, 2], [1], [1], [1]]
    result = [None, None, None, None, 2, None, 3]
    assert base(commands, data) == result


def test_2():
    commands = ["MyLinkedList", "addAtHead",
                "addAtIndex", "get", "deleteAtIndex", "get"]
    data = [[], [1], [1, 2], [1], [1], [1]]
    result = [None, None, None, 2, None, -1]
    assert base(commands, data) == result


def test_3():
    commands = ["MyLinkedList", "get",
                "addAtIndex", "get", "deleteAtIndex", "get", "deleteAtIndex"]
    data = [[], [1], [0, 1], [0], [0], [0], [1]]
    result = [None, -1, None, 1, None, -1, None]
    assert base(commands, data) == result


def test_4():
    commands = ["MyLinkedList", "get"]
    data = [[], [0]]
    result = [None, -1]
    assert base(commands, data) == result


'''
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]
["MyLinkedList", "addAtHead","addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [1, 2], [1], [1], [1]]
["MyLinkedList", "get","addAtIndex", "get", "deleteAtIndex", "get", "deleteAtIndex"]
[[], [1], [0, 1], [0], [0], [0], [1]]
["MyLinkedList", "get"]
[[], [0]]
'''

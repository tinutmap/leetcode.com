from .linked_list import MyLinkedList


def base(command_list, input_list, result):
    a = MyLinkedList()
    output = [None]
    for i in range(1, min(len(command_list), len(input_list))):
        if type(input_list[i]) == type([]):
            value = a.__getattribute__(command_list[i])(*input_list[i])
        else:
            value = a.__getattribute__(command_list[i])(input_list[i])
        if value is not None:
            value = value.value
        output.append(value)
    assert result == output


def test_1():
    command_list = ["MyLinkedList", "addAtHead", "addAtTail",
                    "addAtIndex", "get", "deleteAtIndex", "get"]
    input_list = [[], [1], [3], [1, 2], [1], [1], [1]]
    result = [None, None, None, None, 2, None, 3]
    base(command_list, input_list, result)


def test_2():
    command_list = ["MyLinkedList", "addAtHead", "addAtTail",
                    "addAtIndex", "get", "deleteAtIndex", "get"]
    input_list = [[], [1], [3], [1, 2], [1], [0], [0]]
    result = [None, None, None, None, 2, None, 2]
    base(command_list, input_list, result)


def test_3():
    command_list = ["MyLinkedList", "addAtHead", "addAtTail",
                    "addAtIndex", "get", "deleteAtIndex", "get"]
    input_list = [[], [1], [3], [1, 2], [1], [1], [1]]
    result = [None, None, None, None, 2, None, 3]
    base(command_list, input_list, result)


def test_4():
    command_list = ["MyLinkedList", "addAtHead", "get", "addAtHead", "addAtHead",
                    "deleteAtIndex", "addAtHead", "get", "get", "get", "addAtHead", "deleteAtIndex"]
    input_list = [[], [4], [1], [1], [5], [3], [7], [3], [3], [3], [1], [4]]
    result = [None, None, -1, None, None, None, None, 4, 4, 4, None, None]
    base(command_list, input_list, result)

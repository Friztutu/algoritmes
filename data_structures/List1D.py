import typing


class Node1D:
    __slots__ = 'data', '__next'

    def __init__(self, value):
        self.data = value
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if not (isinstance(obj, Node1D) or obj is None):
            raise TypeError

        self.__next = obj


class List1D:
    __slots__ = ('__head', '__tail', '__len')

    def __init__(self, args=(), reverse=False):
        self.__head = self.__tail = None
        self.__len = 0

        for value in args:
            self.push_back(value) if not reverse else self.push_front(value)

    @property
    def head(self):
        if self.__head:
            return self.__head.data

    @property
    def tail(self):
        if self.__tail:
            return self.__tail.data

    def __iter__(self):
        curr_obj = self.__head
        while curr_obj:
            yield curr_obj.data
            curr_obj = curr_obj.next

    def __len__(self):
        return self.__len

    def __get_node_by_index(self, indx: int):
        curr_obj = self.__head
        curr_indx = 0

        while curr_indx != indx:
            curr_obj = curr_obj.next
            curr_indx += 1

        return curr_obj

    def __getitem__(self, item):
        if not self.__check_index(item):
            raise IndexError('Неверный индекс')

        if item < 0:
            item = len(self) + item

        result = self.__get_node_by_index(item).data

        return result

    def push_back(self, value):
        obj = Node1D(value)

        if self.__head is None:
            self.__head = self.__tail = obj
            self.__len += 1
            return

        curr_obj = self.__head
        while curr_obj:
            if not curr_obj.next:
                break

            curr_obj = curr_obj.next

        curr_obj.next = obj
        self.__tail = obj
        self.__len += 1

    def push_front(self, obj):
        obj = Node1D(obj)
        if self.__head is None:
            self.__head = self.__tail = obj
            self.__len += 1
            return

        obj.next = self.__head
        self.__head = obj
        self.__len += 1

    def pop_front(self):
        if self.__head is None:
            raise ValueError('List1D is empty')

        if self.__tail == self.__head:
            pop_obj = self.__head
            self.__head = self.__tail = None
            self.__len -= 1
            return pop_obj.data

        pop_obj = self.__head
        self.__head = self.__head.next
        self.__len -= 1
        return pop_obj.data

    def pop_back(self):
        if self.__head is None:
            raise ValueError

        if self.__head == self.__tail:
            pop_obj = self.__head
            self.__head = self.__tail = None
            self.__len -= 1
            return pop_obj.data

        pre_tail_obj = self.__get_node_by_index(len(self) - 2)

        pre_tail_obj.next = None
        pop_obj = self.__tail
        self.__tail = pre_tail_obj
        self.__len -= 1
        return pop_obj.data

    def insert(self, index, obj):
        if index < 0:
            index = len(self) - index

        if index == 0:
            self.push_front(obj)
            return

        if index >= len(self):
            self.push_back(obj)
            return

        obj = Node1D(obj)
        prev_obj = self.__get_node_by_index(index - 1)
        next_obj = prev_obj.next
        obj.next = next_obj
        prev_obj.next = obj
        self.__len += 1

    def __check_index(self, item):
        return type(item) == int and -len(self) <= item < len(self)

    def clear(self):
        self.__head = self.__tail = None
        self.__len = 0

    def show_list(self):
        lst_str = ''
        for value in self:
            lst_str += f'{value}->'
        lst_str += 'None'
        return lst_str


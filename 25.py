class RandomListNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.random = None


def clone(p_head):
    if p_head is None:
        return
    current = p_head
    # 将新生成节点插入到原链表中（A, A1，B, B1, C, C1, D, D1）
    while current:
        node = RandomListNode(current.value)
        node.next_node = current.next_node
        current.next_node = node
        current = node.next_node

    # 让新生成节点指向前原节点的随机节点
    current = p_head
    while current:
        node = current.next_node
        if current.random:
            node.random = current.random.next_node
        current = current.next_node

    # 拆分原链表
    current = p_head
    result_node = current.next_node
    while current.next_node:
        node = current.next_node
        current.next_node = node.next_node
        current = node
        if not current:
            return
    return result_node


if __name__ == '__main__':
    head = RandomListNode(1)
    head.next_node = RandomListNode(2)
    head.next_node.next_node = RandomListNode(3)
    head.next_node.next_node.next_node = RandomListNode(4)
    clone_link_list = clone(head)
    print(clone_link_list.value)


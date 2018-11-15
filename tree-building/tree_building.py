class Record():
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    for record in records:
        if record.record_id == 0:
            if record.parent_id != 0:
                raise ValueError('Root node cannot have a parent')
        if record.record_id < record.parent_id:
            raise ValueError('Parent id must be lower than child id')
        if record.record_id == record.parent_id:
            if record.record_id != 0:
                raise ValueError('Tree is a cycle')
    records.sort(key=lambda x: x.record_id)
    tree = [Node(i.record_id) for i in records]
    if records:
        if records[-1].record_id != len(records) - 1:
            raise ValueError('Tree must be continuous')
        if records[0].record_id != 0:
            raise ValueError('Tree must start with id 0')

    for record in records[1:]:
        tree[record.parent_id].children.append(tree[record.record_id])
    return tree[0] if len(tree) > 0 else None

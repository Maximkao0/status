items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

class TreeStore:
    def __init__(self, items):
        self.items = items
        self.key = {}
        self.children = {}

        for i in self.items:
            self.addItem(i)

    def addItem(self, item):
        try:
            id = item['idk']
            self.key[id] = self.items.index(item)
            parentId = self.items[self.key[id]]['parent']
            if parentId in self.key:
                if parentId in self.children:
                    self.children[parentId] += [id]
                else:
                    self.children[parentId] = [id]

        except KeyError as ke:
            print('Error', ke)
            next()

    def getAll(self):
        return self.items

    def getItem(self, id):
        return self.items[self.key[id]]

    def getChildren(self, id):
        result = []
        if id in self.children:
            for i in self.children[id]:
                result += [self.getItem(i)]
        return result

    def  getAllParents(self, id):
        result = [self.getItem(id)]
        parentId = self.items[self.key[id]]['parent']
        if parentId in self.key:
            result += self.getAllParents(parentId)
            return result
        return result


try:
    ts = TreeStore(items)
    print(ts.getAll())
    print(ts.getItem(7))
    print(ts.getChildren(4))
    print(ts.getChildren(5))
    print(ts.getAllParents(7))
except:
    print('compilation error')

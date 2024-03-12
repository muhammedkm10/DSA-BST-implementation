class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if  data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
           self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()



    def deletenode(self,data,curr):
        if self.key is None:
            print("the tree is empty you cant delete")
            return
        if data < self.key:
            if self.lchild:
                self.lchild  = self.lchild.deletenode(data,curr)
            else:
                print('the item is not present in the tree')
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.deletenode(data,curr)
            else:
                print("the node with the given data is not present in the tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.rchild = temp.rchild 
                    self.lchild  = temp.lchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key  = temp.key
                    self.rchild = temp.rchild
                    self.lchild = temp.lchild
                    temp = None
                    return
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.deletenode(data,curr)
        return  self





root =  BST(None)
def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)
u = [1,2,3,4,56,10,7]
for i in u:
    root.insert(i)
i = count(root)
# if i > 1:
#     root.deletenode(10,root.key)
# else:
#     print("you cant delete")

root.deletenode(1,root.key)
root.preorder()


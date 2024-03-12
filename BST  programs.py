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
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self,data):
        if self.key == data:
            print("the item is present in the tree")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("the data is not present in  the tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("the item is not present in the tree")

    def preorder(self):
      print(self.key,end=" ")
      if self.lchild:
          self.lchild.preorder()
      if self.rchild:
          self.rchild.preorder()


    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")


    def delete(self,data,curr):
        if self.key is None:
            print("The tree is empty you can't delete")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print("The data is not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print("The data is not present in the tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                   self.key = temp.key
                   self.rchild = temp.rchild
                   self.lchild = temp.lchild
                   temp = None
                   return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.rchild  = temp.rchild
                    self.lchild  = temp.lchild
                    temp = None
                    return
                self = None
                return temp
            node  = self.rchild
            while node.lchild:
                node = node.lchild
            self.key  = node.key
            self.rchild = self.rchild.delete(node.key,curr)
        return self

    def minimum(self):
        if self.key is None:
            print("The tree is empty")
            return
        else:
            current = self
            while current.lchild:
                current =  current.lchild
            print(current.key)
    def maximum(self):
        if self.key is None:
            print("the tree is empty")
            return
        else:
            current = self
            while current.lchild:
                current = current.lchild
            print(current.key)

    def closestvalue(self,target):
        if self.key is None:
            print("The tree is empty")
            return
        current = self
        closest = self.key
        while current:
            if abs(target - closest) > abs(target - current.key):
                closest = current.key
            if target < current.key:
                current = current.lchild
            elif target > current.key:
                current  = current.rchild
            else:
                break
        return closest

    def inorderforcheck(self):
        result   = []
        if self.lchild:
            result.extend(self.lchild.inorderforcheck())
        result.append(self.key)
        if self.rchild:
            result.extend(self.rchild.inorderforcheck())
        return result


tr = BST(10)

o = [34,33,11,565,34,6,31,234]
for i in o:
    tr.insert(i)

tr.search(31)
tr.preorder()
print("\n")
tr.inorder()
print("\n")
tr.postorder()
print("\n")

def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)
y = count(tr)
if y >1:
    tr.delete(10,tr.key)
else:
    print('you cant do delete operation')
tr.inorder()

print("\n",tr.closestvalue(78))

def check(self):
    if self.key is None:
        print("the tree is empty")
        return
    list1 = self.inorderforcheck()
    print(list1)
    for i  in range(1,len(list1)):
        if list1[i] < list1[i-1]:
            return False
    return True
w = check(tr)
if w:
    print("it is  a binary search tree")
else:
    print("this is not a binary search tree")

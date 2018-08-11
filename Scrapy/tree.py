import csv

class Node(object):
    def __init__(self, data = {}):
        self.name = data.get('name')                #姓名
        self.sex = data.get('sex')                  #年龄
        self.mobile = data.get('mobile')            #手机
        self.address = data.get('address')          #区域
        self.phone = data.get('phone')              #座机
        self.mail = data.get('mail')                #邮箱
        self.number = data.get('number')            #工号
        self.position = data.get('position')        #职位
        self.superior = data.get('superior')        #上级
        self.subordinate = data.get('subordinate', [])  #下级
        self.branch = data.get('branch')            #部门

    def name_change(self, name):
        self.name = name
    def sex_change(self, sex):
        self.sex = sex
    def mobile_change(self, mobile):
        self.mobile = mobile
    def address_change(self, address):
        self.address = address
    def phone_change(self, phone):
        self.phone = phone
    def mail_change(self, mail):
        self.mail = mail
    def number_change(self, number):
        self.number = number
    def position_cahnge(self, position):
        self.position = position
    def superior_add(self, superior):
        self.superior.add(superior)
    def superior_delete(self, superior):
        self.superior.remove(superior)
    def subordinate_add(self, subordinate):
        self.subordinate.append(subordinate)
    def subordinate_delete(self, subordinate):
        self.subordinate.remove(subordinate)
    def branch_add(self, branch):
        self.branch.add(branch)
    def branch_delete(self, branch):
        self.branch.remove(branch)


class Tree(object):
    def __init__(self):
        self.head = Node()

    def append(self, data, name=None):
        if not isinstance(data, Node):
            return False

        if name == None:
            return 'append(data, name=None) 缺少name'

        if name == 'admin':
            data.superior = 'admin'
            self.head = data
            return '添加头结点成功'
        
        result = self.deep_find(name)
        if not result:
            return 'name 节点不存在'
        if not data.superior:
            data.superior = name
        else:
            if data.superior != name:
                return '上级不符合'
        result.subordinate.append(data)
        return '添加成功'


    def deep_find(self, name):
        node = self.head
        if node.name == name:
            return node
        stack_list = []
        visited = []
        stack_list.append(node)
        visited.append(node)
        while len(stack_list) > 0:
            x = stack_list[-1]
            for w in x.subordinate:
                if not w in visited:
                    if w.name == name:
                        return w
                    visited.append(w)
                    stack_list.append(w)
                    break
            if stack_list[-1] == x:
                stack_list.pop()
        return False


    def save(self):
        stack_list = [self.head]
        with open('database.csv', 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['name', 'sex', 'mobile', 'address', 'phone', 'mail', 'number', 'position', 'superior', 'subordinate', 'branch']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            while len(stack_list) > 0:
                node = stack_list[0]
                lists1 = [i.name for i in node.subordinate]
                lists2 = [i for i in node.subordinate]
                data = {'name': node.name,
                        'sex': node.sex,
                        'mobile': node.mobile,
                        'address': node.address,
                        'phone': node.phone,
                        'mail': node.mail,
                        'number': node.mail,
                        'position': node.position,
                        'superior': node.superior,
                        'subordinate': lists1,
                        'branch': node.branch}
                writer.writerow(data)
                stack_list.extend(lists2)
                stack_list.pop(0)


    def read(self):
        t = Tree()
        with open('database.csv', 'r', encoding='utf-8') as csvfile:
            csvfile.readline()
            reader = csv.reader(csvfile)
            print (reader)
            for row in reader:
                data = {'name': row[0],
                        'sex': row[1],
                        'mobile': row[2],
                        'address': row[3],
                        'phone': row[4],
                        'mail': row[5],
                        'number': row[6],
                        'position': row[7],
                        'superior': row[8],
                        'subordinate': [],
                        'branch': row[10]}
                t.append(Node(data), data['superior'])
        return t


def main():
    a = {'name':'a', 'sex':20}
    b = {'name':'b', 'sex':20}
    c = {'name':'c', 'sex':20}
    d = {'name':'d', 'sex':20}
    e = {'name':'e', 'sex':20}
    f = {'name':'f', 'sex':20}
    g = {'name':'g', 'sex':20}
    h = {'name':'h', 'sex':20}

    t = Tree()
    t.append(Node(a), 'admin')
    t.append(Node(b), 'a')
    t.append(Node(c), 'a')
    t.append(Node(d), 'a')
    t.append(Node(e), 'b')
    t.append(Node(f), 'b')
    t.append(Node(g), 'c')
    t.append(Node(h), 'd')
    t.save()

t = Tree()
t = t.read()
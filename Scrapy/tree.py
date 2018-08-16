import csv

class Node(object):
    '''
    节点数据信息
    '''
    def __init__(self, data = {}):
        self.id = data.get('id')                            #ID
        self.name = data.get('name')                        #姓名
        self.inter = data.get('inter')                      #内网账号
        self.sex = data.get('sex')                          #性别
        self.birthday = data.get('birthday')                #生日
        self.JoinTime = data.get('JoinTime')                #入职时间
        self.MPhone = data.get('MPhone')                    #手机
        self.OrgName = data.get('OrgName')                  #组
        self.Position = data.get('Position')                #职位
        self.Tel = data.get('Tel')                          #座机
        self.City = data.get('City')                        #城市
        self.Email = data.get('Email')                      #邮箱
        self.WorkPlaceName = data.get('WorkPlaceName')      #工作地点
        self.superior = data.get('superior')                #上级
        self.subordinate = data.get('subordinate', [])      #下级


class Tree(object):
    def __init__(self):
        self.head = Node()
        self.n = 0

    def append(self, data, name=None):
        '''
        添加节点到多叉树中
        '''
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
        '''
        多叉树深度优先查找
        非递归
        '''
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


    def find(self, inter):
        '''
        多叉树深度优先查找
        非递归
        '''
        node = self.head
        if node.inter.lower() == inter:
            return node
        stack_list = []
        visited = []
        stack_list.append(node)
        visited.append(node)
        while len(stack_list) > 0:
            x = stack_list[-1]
            for w in x.subordinate:
                if not w in visited:
                    if w.inter.lower() == inter:
                        return w
                    visited.append(w)
                    stack_list.append(w)
                    break
            if stack_list[-1] == x:
                stack_list.pop()
        return False


    def save(self):
        '''
        把多叉树中的所有节点保存到文件
        '''
        stack_list = [self.head]
        with open('niu.csv', 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['id', 'name', 'inter', 'sex', 'birthday', 'JoinTime', 'MPhone', 'OrgName', 'Position', 'Tel', 'City', 'Email', 'WorkPlaceName', 'superior', 'subordinate']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            while len(stack_list) > 0:
                node = stack_list[0]
                lists1 = [i.name for i in node.subordinate]
                lists2 = [i for i in node.subordinate]
                data = {'id': node.id,
                        'name': node.name,
                        'inter': node.inter,
                        'sex': node.sex,
                        'birthday': node.birthday,
                        'JoinTime': node.JoinTime,
                        'MPhone': node.MPhone,
                        'OrgName': node.OrgName,
                        'Position': node.Position,
                        'Tel': node.Tel,
                        'City': node.City,
                        'Email': node.Email,
                        'WorkPlaceName': node.WorkPlaceName,
                        'superior': node.superior,
                        'subordinate': lists1,
                        }
                writer.writerow(data)
                stack_list.extend(lists2)
                stack_list.pop(0)


    def gephi(self):
        lista = [self.head]
        listb = []
        sidefile = open('sidefile.csv', 'w', encoding='utf-8', newline='')
        nodefile = open('nodefile.csv', 'w', encoding='utf-8', newline='')
        sidewriter = csv.writer(sidefile, delimiter=',')
        nodewriter = csv.writer(nodefile, delimiter=',')
        nodewriter.writerow(['Id', 'Lable', 'Size'])
        sidewriter.writerow(['Source', 'Target', 'Weight'])
        n = self.n - 1
        while True:
            while len(lista) > 0:
                node = lista[0]
                nodewriter.writerow([node.name, node.sex, n * n * n])
                lists1 = [i.name for i in node.subordinate]
                lists2 = [i for i in node.subordinate]
                for name in lists1:
                    sidewriter.writerow([node.name, name, n * n])
                listb.extend(lists2)
                lista.pop(0)
            n -= 1
            if len(listb) > 0:
                lista = listb
                listb = []
            else:
                break



    def read(self):
        '''
        读取文件中的数据到多叉树
        '''
        t = Tree()
        with open('database.csv', 'r', encoding='utf-8') as csvfile:
            csvfile.readline()
            reader = csv.reader(csvfile)
            print(reader)
            read_list = []
            for row in reader:
                data = {'id': row[0],
                        'name': row[1],
                        'inter': row[2],
                        'sex': row[3],
                        'birthday': row[4],
                        'JoinTime': row[5],
                        'MPhone': row[6],
                        'OrgName': row[7],
                        'Position': row[8],
                        'Tel': row[9],
                        'City': row[10],
                        'Email': row[11],
                        'WorkPlaceName': row[12],
                        'superior': row[13],
                        'subordinate': [],}
                node = Node(data)
                if len(read_list) == 0:
                    t.append(node, node.superior)
                    read_list.append(node)
                else:
                    head = read_list[0]
                    while node.superior != head.name:
                        read_list.pop(0)
                        head = read_list[0]
                    head.subordinate.append(node)
                    read_list.append(node)
        return t


    def level(self):
        lista = [self.head]
        listb = []
        self.n = 0
        while True:
            while len(lista) > 0:
                node = lista[0]
                lists = [i for i in node.subordinate]
                listb.extend(lists)
                lista.pop(0)
            self.n += 1
            if len(listb) > 0:
                lista = listb
                listb = []
            else:
                break

def main():
    t = Tree()
    t = t.read()
    t.level()
    t.gephi()

main()

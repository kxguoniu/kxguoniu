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
        self.subordinate = data.get('subordinate')  #下级
        self.branch = data.get('branch')            #部门

    def name_change(name):
        self.name = name
    def sex_change(sex):
        self.sex = sex
    def mobile_change(mobile):
        self.mobile = mobile
    def address_change(address):
        self.address = address
    def phone_change(phone):
        self.phone = phone
    def mail_change(mail):
        self.mail = mail
    def number_change(number):
        self.number = number
    def position_cahnge(position):
        self.position = position
    def subordinate_add(subordinate):
        self.subordinate.add(subordinate)
    def subordinate_delete(subordinate):
        self.subordinate.remove(subordinate)
    def superior_add(superior):
        self.superior.add(superior)
    def superior_delete(superior):
        self.superior.remove(superior)
    def branch_add(branch):
        self.branch.add(branch)
    def branch_delete(branch):
        self.branch.remove(branch)


class Tree(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return (self.length == 0)

    def append(self, data, name=None):
        if not isinstance(dataOrNode, Node):
            return False

        if name == None:
            self.head = data
            return True
        
        node = self.head
        result = deep_find(node, name)
        if not result:
            return 'name 节点不存在'
        result.subordinate.append(dataOrNode)
        return True

            

    def deep_find(self, node, value, path=[]):
        stack_list = []
        visited = []
        stack_list.append(node)
        visited.append(node)
        while len(stack_list) > 0:
            x = stack_list[-1]
            for w in x.subordinate:
                if not w in visited:
                    print(w.name)
                    if w.name == value:
                        return w
                    visited.append(w)
                    stack_list.append(w)
                    break
            if stack_list[-1] == x:
                stack_list.pop()

        return False
# 导入Student类
from  student import Student


class StudentManager:
    """
    定义一个学生管理类,在这个类中定义显示菜单和对学生进行增删改查的方法
    """

    def __init__(self):
        # 定义一个类属性, 用来存储系统中的Student对象
        self.students_dict = {}

    def startup(self):
        """
        学生管理系统的入口,系统一启动的时候就应该调用这个方法
        """

        # 在系统一启动的时候就从文件中读取数据,把数据保存到students_dict中
        self.load_from_file("data.txt")

        # 循环1,2,3步骤
        while True:
            # 1.调用StudentManager类中显示菜单的功能
            self.show_menu()

            # 2.提示录入菜单编号
            menu_code = int(input("请录入您选择的功能:"))

            # 3.根据菜单编号调用对应的功能
            if menu_code == 1:
                # print("调用 1.添加学生 的功能")
                self.add_student()
            elif menu_code == 2:
                # print("调用 2.显示全部 的功能")
                self.show_all()
            elif menu_code == 3:
                # print("调用 3.查询学生 的功能")
                self.find_student()
            elif menu_code == 4:
                # print("调用 4.修改学生 的功能")
                self.update_student()
            elif menu_code == 5:
                # print("调用 5.删除学生 的功能")
                self.delete_student()
            elif menu_code == 0:
                print("退出系统")

                # 在退出系统时,把学生列表中的数据都保存到文件中
                self.save_to_file("data.txt")
                break
            else:
                print("录入的菜单编号有误,请重新录入!!!\n")

    @staticmethod
    def show_menu():
        """
        显示菜单:
        ******************************
        欢迎使用【学生管理系统】 V1.0
        1.添加学生
        2.显示全部
        3.查询学生
        4.修改学生
        5.删除学生

        0.退出系统
        ******************************
        """
        print("*" * 30)
        print("欢迎使用【学生管理系统】 V1.0")
        print("1.添加学生")
        print("2.显示全部")
        print("3.查询学生")
        print("4.修改学生")
        print("5.删除学生")
        print()
        print("0.退出系统")
        print("*" * 30)

    def add_student(self):
        """
        添加一个学生
        """
        # 提示并录入学生的3个信息
        id = input("请录入学号:")
        name = input("请录入姓名:")
        score = input("请录入考试分数:")

        # 把字典添加到列表中
        if id in self.students_dict.keys():
            print("学生已存在!!!")
            return

        else:
            # 把3个信息封装到一个Student对象中
            student = Student(id, name, score)
            self.students_dict[id] = student

            # 提示"添加成功!"
            print("添加学生" + id + "成功!\n")

        print(self.students_dict)

    def show_all(self):

        # 判断系统中是否有学生信息
        if len(self.students_dict) <= 0:
            # 如果没有,就提示"系统中还没有学生信息!!!"
            print("系统中还没有学生信息!!!\n")
        else:
            # 如果有
            # 先打印表头,一条线
            print("学号".ljust(14) + "姓名".ljust(15) + "分数".ljust(15))
            print("-" * 45)
            # 4.2 遍历列表,打印每个学生,一个学生打印成干一行
            for student in self.students_dict.values():
                id = student.id
                name = student.name
                score = student.score
                print(id.ljust(15) + name.ljust(15) + score.ljust(15))
            # 4.3 打印一条线
            print("-" * 45)

    def find_student(self):
        """
        查询一个学生
        """

        # 提示录入一个姓名
        input_id = input("请录入一个学号:")
        # 遍历列表
        if input_id not in self.students_dict.keys():
            # 如果比较了一遍没有发现有姓名一样的学生,就提示在系统中没有找到此学生
            print("在系统中没有找到此学生!!!\n")
            return
        else:
            # 在系统中得到该学生对象
            student = self.students_dict[input_id]
            # 如果一样就打印
            print("学号".ljust(14) + "姓名".ljust(15) + "分数".ljust(15))
            print("-" * 45)
            id = student.id
            name = student.name
            score = student.score
            print(id.ljust(15) + name.ljust(15) + score.ljust(15))
            print("-" * 45)

    def update_student(self):
        """
        修改一个学生
        """

        # 1.提示录入一个学号
        input_id = input("请录入一个学号:")

        # 判断系统中是否有该学号对应的学生
        if input_id not in self.students_dict.keys():
            # 如果没有找到该学生
            print("在系统中没有找到此学生!!!\n")
            return
        else:
            # 如果找到了就打印该学生
            # 在系统中得到该学生对象
            student = self.students_dict[input_id]

            # 获得要修改的信息
            new_name = input('请输入新名字:')
            new_score = input('请输入新分数:')

            # 修改学生的姓名和分数
            student.name = new_name
            student.score = new_score

            # 提示修改变成功
            print("修改%s成功" % input_id)

    def delete_student(self):
        """
        删除一个学生
        """

        # 提示录入一个学号
        input_id = input("请录入一个学号:")

        # 判断系统中是否有该学号对应的学生
        if input_id not in self.students_dict.keys():
            # 如果没有找到
            print("在系统中没有找到此学生!!!\n")
            return
        else:
            # 如果找到了
            # 删除学生
            del self.students_dict[input_id]
            print("删除成功!!!\n")

    def save_to_file(self, file):
        """
        把列表中的数据写到指定的文件中
        :param file: 文件
        """

        # 得到字典中的所有学生
        student_list = self.students_dict.values()

        # 把所有学生 都写到一个文件中,一个学生写一行
        f = open(file, "w", encoding="UTF-8")

        for student in student_list:

            # 一个学生写一行
            f.write(str(student)+"\n")

        # 关闭文件
        f.close()

    def load_from_file(self, file):
        """
        从指定的文件中读取,并返回数据
        :param file:
        :return: 返回从文件中读出来的数据
        """
        f = open(file, "r", encoding="UTF-8")
        for line in f.readlines():
            # 得到一行的字符串,去掉最后的换行符"\n"
            student_info = line[:-1].split(",")
            # 得到学生的3个信息
            id = student_info[0]
            name = student_info[1]
            score = student_info[2]
            # 创建一个学生对象
            student = Student(id, name, score)
            # 在字典中保存学生对象
            self.students_dict[id] = student

        # 关闭文件
        f.close()
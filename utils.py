# 通用断言函数
import json


def assert_common(httpcode, success, code, message, response, self):
    self.assertEqual (httpcode, response.status_code)  # 断言响应状态码
    self.assertEqual (success, response.json ().get ("success"))  # 断言success
    self.assertEqual (code, response.json ().get ("code"))  # 断言code
    self.assertIn (message, response.json ().get ("message"))  # 断言message


# 定义一个读取员工模块数据的函数,接受文件路径和要读取的文件接口内容
def read_emp_data(filename, name):
    # 打开文件
    with open(filename, mode="r", encoding="utf-8") as f:
        # 用json加载
        jsonData = json.load(f)
        # 读取数据
        emp_data = jsonData.get(name)
        # 定义一个空列表
        result_list = []
        #添加
        result_list.append(tuple(emp_data.values()))
        #打印
        print(result_list)
        return result_list
if __name__ == '__main__':
    import app
    filename = app.PATH + "/data/emp_data.json"
    read_emp_data(filename,"add_emp")  # 添加员工
    read_emp_data (filename, "query_emp")  # 查询员工
    read_emp_data (filename, "modify_emp")  # 修改员工
    read_emp_data (filename, "delete_emp")  # 删除员工




























# 读取登录数据的函数
# 1 定义读取数据的函数，并从外界接收文件名
def read_login_data(filename):
    # 2 使用内置函数open打开外界传入的文件名
    with open (filename, mode='r', encoding='utf-8') as f:
        # 3 使用内置模块json加载文件
        jsonData = json.load (f)
        # 定义一个存放数据的空列表
        result_list = list ()
        # 4 读取每一组数据，并按照parameterized的要求，拼接数据成一个嵌套元组的形式
        for login_data in jsonData:
            result_list.append (tuple (login_data.values ()))
        # 5 打印结果，并return 返回
        print (result_list)
        return result_list


if __name__ == '__main__':
    import app

    filename = app.PATH + "/data/login_data.json"
    print ("filename的路径为PATH：", filename)
    read_login_data (filename)

# 多线程
import os
import threading

def copy_file(file_name,source_dir,dest_dir):
   
   # 拼接源文件和目标文件的路径
   source_path = source_dir + "/" + file_name
   dest_path = dest_dir + "/" + file_name
   
   # 打开源文件和目标文件
   with open(source_path,"rb") as source_file:
       with open(dest_path,"wb") as dest_file:

           # 循环拷贝源文件到目标文件
           while True:
               # 读取源文件内容
               file_data = source_file.read(1024)
               if file_data:
                   # 把源文件内容写入目标文件中
                   dest_file.write(file_data) 
               else:
                   break

if __name__ == "__main__":

    # 定义源文件夹所在路径和目标文件夹所在路径
    source_dir = r"E:\picture"
    dest_dir = r"C:\Users\Administrator\Desktop\picture"

    # 创建目标文件夹
    try:
        # 如果没有就创建
        os.mkdir(dest_dir)

    except:
        print("目标文件已存在")

    # 通过 os.listdir 获取源文件夹中文件的列表
    file_list = os.listdir(source_dir)
    print(file_list)

    # for循环，遍历列表，获取需要拷贝的文件
    for file_name in file_list:
        # copy_file(file_name,source_dir,dest_dir) # 单任务

        # 创建子线程实现多任务拷贝
        sub_thread = threading.Thread(target=copy_file,args=(file_name,source_dir,dest_dir)) # 多任务
        
        # 启动子线程
        sub_thread.start()

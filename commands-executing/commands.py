import subprocess

def execute_w():
    subprocess.run(["w"])

def execute_list_of_users():
    cmd = "awk -F':' '{print $1}' /etc/passwd"
    subprocess.run(cmd.split())

def execute_list_of_users_read():
    data = open('/etc/passwd')
    print(list(filter(lambda x: x.split()[0], data.readlines())))
    data.close()

execute_list_of_users_read()
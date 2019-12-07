import subprocess


def execute_w():
    subprocess.run(["w"])

def execute_list_of_users():
    cmd = "awk -F':' '{print $1}' /etc/passwd"
    subprocess.run(cmd.split())

def execute_list_of_users_read():
    data = open('/etc/passwd')
    print(list(map(lambda x: x.split(':')[0], data.readlines())))
    data.close()

def check_exist_user(user):
    '''
    check if target user is exist
    '''
    if user is None:
        raise Exception('user is not defined')
    f = open('/etc/passwd')
    data = f.readlines()
    f.close()
    return len([x for x in data if x.split(':')[0] == user]) > 0

print(check_exist_user('postgres'))
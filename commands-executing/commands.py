import subprocess

def execute_w():
    subprocess.run(["w"])

def execute_list_of_users():
    cmd = "awk -F':' '{print $1}' /etc/passwd"
    subprocess.run(cmd.split())

execute_list_of_users()
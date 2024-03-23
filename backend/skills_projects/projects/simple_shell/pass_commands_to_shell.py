#!/usr/bin/env python3
import subprocess

def pass_cmd_to_shell(cmds):
    malicious_cmds = ['rm -rf', 'mv', 'dd', 'chmod', 'chown', 'shutdown', 'reboot', 'kill']
    if any(malicious in cmds for malicious in malicious_cmds):
        return "Error: Malicious command detected"

    # Run the shell inside a Docker container
    docker_command = f'docker run --rm simple_shell bash -c "echo \'{cmds}\' | ./myshell"'
    process = subprocess.Popen(docker_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        return stderr.decode()
    else:
        return stdout.decode()
    

if __name__=="__main__":
   while True:
         cmds = input("Enter command: ")
         print(pass_cmd_to_shell(cmds))

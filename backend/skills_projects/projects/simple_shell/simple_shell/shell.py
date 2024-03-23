#!/usr/bin/python3
import os
import pty
import subprocess

master, slave = pty.openpty()

# Start your custom shell as the PTY process
process = subprocess.Popen(['./myshell'], stdin=slave, stdout=slave, stderr=slave, start_new_session=True)

# Close the slave PTY file descriptor in the parent process
os.close(slave)

# Now you can interact with your custom shell through the master PTY
while True:
    try:
        output = os.read(master, 1024).decode()
        # Process the output as needed
        print(output)
        
        # Example: Sending input to the custom shell
        command = input("Enter command: ")
        os.write(master, command.encode() + b'\n')
    except KeyboardInterrupt:
        break

# Close the master PTY file descriptor
os.close(master)

# Wait for the shell process to terminate
process.wait()

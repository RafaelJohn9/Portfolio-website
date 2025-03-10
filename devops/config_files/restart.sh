#!/usr/bin/bash
# used to relaunch the server

DOCKER_ID=$(docker ps | awk 'NR==2 {print $1}')
# this part of the script kills all processes on needed ports
sudo docker stop "$DOCKER_ID"

# Function to kill processes on a given port
kill_process_on_port() {
    port="$1"
    echo "Killing processes on port $port"
    pid_list=$(sudo lsof -ti :$port)
    if [ -z "$pid_list" ]; then
        echo "No processes found on port $port"
    else
        sudo kill -9 $pid_list
        echo "Processes killed on port $port"
    fi
}

# Call the function for port 5001
kill_process_on_port 5001

# Call the function for port 3000
kill_process_on_port 3000

echo "Process killing script completed"




# Restarting the proccesses
cd ~/Portfolio*/backend/user
~/Portfolio*/backend/user/install_master.sh

cd ~/Portfolio*/backend/skills*
tmux new-session -d -s myapi 'gunicorn -b 127.0.0.1:5001 run:app'


cd ~/Portfolio*/frontend
tmux new-session -d -s frontend 'serve -s build'

from fabric.api import task, env, put
import os

# Define the IP address of your web server
env.hosts = ["34.224.3.244"]

@task
def deploy_empty_file():
    # Path to the empty text file on your local machine
    local_file_path = 'test_of_fab'

    # Remote directory to upload the empty text file to
    remote_dir = '~/'

    # Check if the local file exists
    if not os.path.exists(local_file_path):
        print(f"Local file not found: {local_file_path}")
        return False

    # Upload the empty text file to the server
    for host in env.hosts:
        remote_file_path = os.path.join(remote_dir, os.path.basename(local_file_path))
        put(local_file_path, remote_file_path)
        print(f"File uploaded to: {remote_file_path}")

    print("Deployment successful!")
    return True

import subprocess
def main():
    # Command to run
    command = ["ls", "-l"] # For unix like systems
    # command = ["cmd", "/c", "dir"] # For Windows
    # Create and start the child process
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
    # Wait for the child process to complete
    stdout, stderr = process.communicate()
    # Output the results
    print("Child process finished execution.")
    print(f"Standard Output:\n{stdout.decode()}")
    if stderr:
        print(f"Standard Error:\n{stderr.decode()}")
if __name__ == "__main__":
    main()        
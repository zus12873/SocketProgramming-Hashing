import os
import time
from socket import AF_INET, SOCK_STREAM, socket
from subprocess import Popen
import select

# Change to the appropriate directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
os.chdir('Answers')

inOut = [
    (['0'], '0'),
    (['0', '0'], '00'),
    (['hell0'], '0'),
    (['Hell0', 'Pe0ple 0f the W0rld'], '0000')
]

passed = 0

for i, o in inOut:
    print(f"Starting test case: {i}")
    # Start the server process
    proc = Popen(["python", "2.py"])
    time.sleep(1)  # Ensure server is up and running

    with socket(AF_INET, SOCK_STREAM) as s:
        try:
            s.connect(('127.0.0.1', 8080))
            print('Connected to server')
            for inp in i:
                s.sendall(inp.encode())  # Send data to the server
            time.sleep(0.1)  # Allow time for the server to process

            # Use select to wait for the server's response
            ready_to_read, _, _ = select.select([s], [], [], 1.0)
            if ready_to_read:
                o1 = s.recv(1024).decode()
                if o1 == o:
                    print(f"Test case {i} passed")
                    passed += 1
                else:
                    print(f"Test case {i} failed: expected {o}, got {o1}")
            else:
                print(f"Test case {i} failed: No response from server")
        except Exception as e:
            print(f"Test case {i} encountered an error: {e}")
        finally:
            s.close()

    # Terminate the server process
    proc.terminate()
    proc.wait()

print(f"TASK 2: {passed}/{len(inOut)}")

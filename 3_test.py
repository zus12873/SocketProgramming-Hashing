import os
import time
from socket import AF_INET, SOCK_STREAM, socket
from subprocess import Popen
import select

def start_server():
    """Start the server in a subprocess."""
    return Popen(["python", "Answers/3.py"])

def setup_sockets():
    """Set up two client sockets for communication."""
    s1 = socket(AF_INET, SOCK_STREAM)
    s2 = socket(AF_INET, SOCK_STREAM)
    s1.connect(('127.0.0.1', 8080))
    s2.connect(('127.0.0.1', 8080))
    s1.setblocking(False)
    s2.setblocking(False)
    return s1, s2

def test_communication(actions):
    """Test communication between two clients based on a sequence of actions."""
    s1, s2 = setup_sockets()
    scks = [s1, s2]
    toRead = ["", ""]
    temp = True

    for action, sockNo in actions:
        try:
            if action is None:
                # Wait for data to be ready to read using select
                ready_to_read, _, _ = select.select([scks[sockNo]], [], [], 1.0)
                if ready_to_read:
                    dt = scks[sockNo].recv(1024).decode()
                    if toRead[sockNo] != dt:
                        temp = False
                        break
            else:
                # Send data to the other socket
                scks[sockNo].sendall(action.encode())
                toRead[(sockNo + 1) % 2] += action
        except Exception as e:
            print(f"Error during communication: {e}")
            temp = False
            break

    s1.close()
    s2.close()
    return temp

def run_tests():
    """Run all the tests and track how many pass."""
    inp = [
        [('Hello', 0), (None, 1)],
        [('Hi', 1), (None, 0)],
        [('Hello', 0), (None, 1), ('How are you?', 1), (None, 0)],
        [('Hello', 0), ('Hi, ', 1), (None, 1), ('How are you?', 1), (None, 0)],
    ]
    
    passed = 0
    for i in inp:
        proc = start_server()
        time.sleep(1)  # Give the server some time to start

        if test_communication(i):
            passed += 1
            print(f"Test case {i} passed")

        # Clean up the server process
        proc.terminate()
        proc.wait()

    print(f'TASK 3: {passed}/{len(inp)}')

if __name__ == "__main__":
    run_tests()

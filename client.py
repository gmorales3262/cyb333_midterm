#!/usr/bin/env python3
"""
Simple TCP client for CYB midterm.
Connects to the server, sends a message, receives a response.
Demonstrates error handling when server is not running.
"""

import socket

HOST = "127.0.0.1"  # Server address
PORT = 5050         # Must match server port

def main():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print(f"[CLIENT] Connecting to {HOST}:{PORT} ...")
        client_socket.connect((HOST, PORT))
        print("[CLIENT] Connected successfully.")

        message = "Hello from client!"
        print(f"[CLIENT] Sending: {message}")
        client_socket.sendall(message.encode("utf-8"))

        data = client_socket.recv(1024)
        response = data.decode("utf-8").strip()
        print(f"[CLIENT] Received from server: {response}")

    except ConnectionRefusedError:
        print("[CLIENT] Connection refused. Is the server running?")
    except OSError as e:
        print(f"[CLIENT] Socket error: {e}")
    except Exception as e:
        print(f"[CLIENT] Unexpected error: {e}")
    finally:
        print("[CLIENT] Closing socket.")
        client_socket.close()

if __name__ == "__main__":
    main()

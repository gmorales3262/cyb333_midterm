#!/usr/bin/env python3
"""
Simple TCP echo server for CYB midterm.
Listens for a single client, echoes messages, then shuts down cleanly.
"""

import socket

HOST = "127.0.0.1"  # Listen on localhost only
PORT = 5050         # Non-privileged port

def main():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allow quick restart if socket is in TIME_WAIT
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((HOST, PORT))
        print(f"[SERVER] Listening on {HOST}:{PORT} ...")
        server_socket.listen(1)

        # Wait for a connection
        conn, addr = server_socket.accept()
        print(f"[SERVER] Connection established from {addr}")

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    print("[SERVER] Client disconnected.")
                    break

                message = data.decode("utf-8").strip()
                print(f"[SERVER] Received from client: {message}")

                response = f"Server received: {message}"
                conn.sendall(response.encode("utf-8"))
                print(f"[SERVER] Sent to client: {response}")

    except KeyboardInterrupt:
        print("\n[SERVER] Interrupted by user. Shutting down.")
    except OSError as e:
        print(f"[SERVER] Socket error: {e}")
    except Exception as e:
        print(f"[SERVER] Unexpected error: {e}")
    finally:
        server_socket.close()
        print("[SERVER] Socket closed. Goodbye.")

if __name__ == "__main__":
    main()

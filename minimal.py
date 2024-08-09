import socket


ZOOM_IN = b"\x01\x00\x81\x01\x04\x07\x02\xFF\x00\x00\x00"
ZOOM_OUT = b"\x01\x00\x81\x01\x04\x07\x03\xFF\x00\x00\x00"
ZOOM_STOP = b"\x01\x00\x81\x01\x04\x07\x00\xFF\x00\x00\x00"
VER_INQ =  b"\x01\x00\x81\x09\x00\x02\xFF\x00\x00\x00\x00"
ZOOM_INQ = b"\x01\x00\x81\x09\x04\x47\xFF\x00\x00\x00\x00"



# === CLIENT ===
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("10.1.3.78", 1000))
    # s.bind(('', 0))

    s.sendall(ZOOM_INQ)
    data = s.recv(4096)
    printable = " ".join(f'{b:02x}' for b in data)
    print(printable)


# === SERVER ===
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(('', 1569))
#     s.sendto(ZOOM_IN, ("10.1.3.78", 1569))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             data = conn.recv(1024)
#             print(data)
#             if not data:
#                 break
#             conn.sendall(data)
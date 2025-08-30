from collections import deque, defaultdict, Counter

logs = [
    ("192.168.1.1", 1),
    ("192.168.1.2", 2),
    ("192.168.1.1", 3),
    ("192.168.1.1", 5),
    ("192.168.1.1", 8),
    ("192.168.1.2", 15),
    ("10.0.0.1", 16),
    ("10.0.0.1", 16),
    ("10.0.0.1", 16),
    ("10.0.0.1", 16),
]


logs = deque(logs, maxlen=10)
logs = Counter([ip[0] for ip in logs])

for ip, ip_count in logs.items():
    if ip_count >= 3:
        print(f"{ip} || {ip_count}-time spammed !!!")

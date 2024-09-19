import sys

first_name = sys.argv[1]
last_name = sys.argv[2] if len(sys.argv) >= 3 else ""


print(f"{first_name} {last_name}")

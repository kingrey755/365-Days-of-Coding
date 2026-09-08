import random
systems = ["CPU", "MEMORY", "NETWORK", "STORAGE", "CORE"]
severity = ["LOW", "WARNING", "CRITICAL"]
status = ["STABLE", "UNSTABLE", "CORRUPTED", "OVERLOADED"]
print(f"SYSTEM: {random.choice(systems)}\nSTATUS: {random.choice(severity)}\nERROR: ERR-{random.randint(1000,9999)}\nSIGNAL: {random.choice(status)}!!!!!!!!")

import time
import sys
import random

# Number of times to inject logs
INJECTION_COUNT = 5 # Inject 5 sets of logs (errors + warnings)

# Delay between injections (seconds)
INJECTION_DELAY = 10

# Nginx error patterns (Nginx logs to stdout by default, so we'll simulate an application error)
# For Nginx to truly log an error, it needs to go to stderr. We'll simulate app errors.
error_messages = [
    "ERROR: Upstream connection timed out for service backend-api.example.com",
    "CRITICAL: Failed to connect to database at 10.0.0.5: Connection refused.",
    "ERROR: Invalid request payload received from client IP 192.168.1.100.",
    "WARNING: Deprecated API endpoint /v1/old_feature used by client.",
    "ERROR: Disk space low on /var/log/nginx. 90% utilization.",
    "WARNING: High CPU usage detected for worker process 3."
]

print("Starting log injection into Nginx (simulated application errors/warnings).")
print(f"Injecting {INJECTION_COUNT} times with {INJECTION_DELAY} second delay.")

for i in range(INJECTION_COUNT):
    error_log = random.choice([m for m in error_messages if m.startswith("ERROR") or m.startswith("CRITICAL")])
    warning_log = random.choice([m for m in error_messages if m.startswith("WARNING")])

    # Print to stderr for Nginx to pick it up as an error/warning
    # Nginx by default logs stdout to info, stderr to error.
    print(f"{error_log}", file=sys.stderr)
    print(f"{warning_log}", file=sys.stderr)
    print(f"INFO: Regular activity log line {i+1}") # A regular log line

    print(f"--- Injected logs {i+1}/{INJECTION_COUNT} ---")
    time.sleep(INJECTION_DELAY)

print("Log injection complete.")

import subprocess

print("===================================")
print("DevSecOps Dependency Scanner")
print("===================================")

print("Running security scan...\n")

subprocess.run(["python3", "-m", "pip_audit"])

print("\nScan finished. Starting dependency vulnerability scan...")


print("Scan completed.")

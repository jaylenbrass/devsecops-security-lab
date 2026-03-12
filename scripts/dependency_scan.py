import subprocess

print("===================================")
print("DevSecOps Dependency Scanner")
print("===================================")

print("Running security scan...\n")

subprocess.run(["pip-audit"])

print("\nScan finished. Starting dependency vulnerability scan...")

subprocess.run(["pip-audit"])

print("Scan completed.")

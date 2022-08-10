import subprocess
"""
p = subprocess.run(["python.exe","-V"], capture_output=True, encoding="cp850")

print("Codigo de retorno", p.returncode)
print("Standar Output", p.stdout)
print("Standar Error", p.stderr)
"""

p = subprocess.run(["ipconfig", "/all"], capture_output=True, encoding="cp850")

print("Codigo de retorno", p.returncode)
print("Standar Output", p.stdout)
print("Standar Error", p.stderr)

p = subprocess.run("hostname", capture_output=True, encoding="cp850")

print("Codigo de retorno", p.returncode)
print("Standar Output", p.stdout)
print("Standar Error", p.stderr)
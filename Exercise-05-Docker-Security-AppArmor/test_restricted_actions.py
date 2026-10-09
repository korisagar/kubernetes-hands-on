import docker

client = docker.from_env()

print("Starting container with AppArmor profile for security testing...")
container = client.containers.run(
    "flask-apparmor",
    ports={'5000/tcp': 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)

print(f"Container started: {container.short_id}")

# Test restricted action 1: attempting to read /etc/passwd
print("\n[TEST 1] Attempting to read /etc/passwd (restricted by AppArmor rule: deny /etc/** r):")
exit_code, output = container.exec_run("cat /etc/passwd")
print(f"Attempt to read /etc/passwd -> Exit Code: {exit_code}, Output: {output.decode().strip() or '[ACCESS DENIED]'}")

# Test restricted action 2: attempting to execute /bin/bash
print("\n[TEST 2] Attempting to execute /bin/bash (restricted by AppArmor rule: deny /bin/** rmix):")
exit_code, output = container.exec_run("/bin/bash")
print(f"Attempt to execute /bin/bash -> Exit Code: {exit_code}, Output: {output.decode().strip() or '[EXECUTION DENIED - Permission Denied]'}")

# Clean up
container.stop()
container.remove()
print("\nSecurity testing complete. Container stopped and removed.")

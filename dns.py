from requests import get
import subprocess

working_directory = "/home/peppo/peppoflix.github.io"

with open(f"{working_directory}/ip.txt", "r") as f:
    old_ip = f.read().strip()

new_ip = get('https://api.ipify.org').text

html = f"""<!DOCTYPE html>
<meta charset="utf-8">
<title>Peppoflix</title>
<meta http-equiv="refresh" content="0; URL=http://{new_ip}:8096/">
<link rel="canonical" href="http://{new_ip}:8096/">"""

if old_ip != new_ip:
    print(f"IP address has changed\n{old_ip} -> {new_ip}\nUpdating\n")
    subprocess.run(f"echo {new_ip} > {working_directory}/ip.txt", shell=True)
    subprocess.run(f"echo '{html}' > {working_directory}/index.html", shell=True)
    subprocess.run("git add index.html ip.txt", shell=True)
    subprocess.run('git commit -m "update ip"', shell=True)
    subprocess.run("git push", shell=True)
else:
    print("IP address has not changed")

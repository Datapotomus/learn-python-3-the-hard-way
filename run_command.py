import subprocess

result=subprocess.run(["ls", "-lh"], stdout=subprocess.PIPE)
print(result.stdout)
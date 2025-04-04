import subprocess

print("Add Commit Push")
print("Executing \"git status\":")
print("")

# Run the git status command
resultGitStatus = subprocess.run(["git", "status"], capture_output=True, text=True)
print(resultGitStatus.stdout) 

# Executing git add.
print("Executing \"git add -A\":")
print("")

# Run the git add command
resultGitAdd = subprocess.run(["git", "add", "-A"], capture_output=True, text=True)
print(resultGitAdd.stdout)
print("STDERR:") 
print(resultGitAdd.stderr)

# Executing git commit.
print("Executing \"git commit -m\":")
print("")

# Run the git commit command
message = "\"Update files.\""
resultGitCommit = subprocess.run(["git", "commit", "-m", message], capture_output=True, text=True)
print(resultGitCommit.stdout)
print("STDERR:") 
print(resultGitCommit.stderr)

# Executing git push.
print("Executing \"git push\":")
print("")

# Run the git push command
resultGitPush = subprocess.run(["git", "push"], capture_output=True, text=True)
print(resultGitPush.stdout)
print("STDERR:") 
print(resultGitPush.stderr)

#print("STDERR:") 
#print(result.stderr)
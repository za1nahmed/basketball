import subprocess
import sys

print("Add Commit Push")
print("Executing \"git status\":")
print("")

# Commands to be run
queued_commands = [
    'git status',
    'git add -A',
    f'git commit -m "{sys.argv[2]}"' if len(sys.argv) == 3 else 'git commit -m "Update files."',
    'git push'
]

# Print queued commands
print("The following Git commands will be executed:")
for cmd in queued_commands:
    print(f"  {cmd}")

# Ask for confirmation
confirm = input("\nDo you want to proceed? (y/n): ").strip().lower()
if confirm != 'y':
    print("Operation cancelled by the user.")
    sys.exit(0)

# Run the git status command
resultGitStatus = subprocess.run(["git", "status"], capture_output=True, text=True)
print(resultGitStatus.stdout) 

# Executing git add.
print("Executing \"git add -A\":")

# Run the git add command
resultGitAdd = subprocess.run(["git", "add", "-A"], capture_output=True, text=True)
print(resultGitAdd.stdout)
print("")

# Executing git commit.
print("Executing \"git commit -m\":")
print("")

# Run the git commit command
message = "\"Update files.\""
if len(sys.argv) == 3:
    message = sys.argv[2]
    print (message)

resultGitCommit = subprocess.run(["git", "commit", "-m", message], capture_output=True, text=True)
print(resultGitCommit.stdout)
print("")

# Executing git push.
print("Executing \"git push\":")
print("")

# Run the git push command
resultGitPush = subprocess.run(["git", "push"], capture_output=True, text=True)
print(resultGitPush.stdout)
print("")
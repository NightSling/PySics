import git

# Look at the current repo
repo = git.Repo(search_parent_directories=True)

# Get the last commit on the repo
last_commit = repo.head.commit

# Get the commit message from the last commit
commit_message = last_commit.message

# Split the commit message with character '-' and get the first part as a id
commit_id = int(commit_message.split('-')[0].strip())

# Ask the user for a new commit message
new_commit_message = input('Enter a new commit message: ')

# Create a new commit id by incrementing old one by 1 
new_commit_id = commit_id + 1

# Format the new commit id and new commit message
new_commit_message = '{}-{}'.format(new_commit_id, new_commit_message)

# Git add every changes
repo.git.add(A=True)

# Git Commit with new commit message
repo.git.commit(m=new_commit_message)

# Print out the new commit log
print(repo.git.log())

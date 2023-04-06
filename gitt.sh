#!/bin/bash

#repo_dir="/home/ade/ALX_PRO/alx-system_engineering-devops"

# Change to the repo directory
# Loop through all directories in the repo
for dir in */; do
    # Change to the directory
    cd "$dir" || continue

    # Check if there are changes today
    if [[ "$(git log --since='today')" ]]; then
        # Get the directory name
        dir_name="$(basename "$dir")"

        # Generate the commit message
        message="Update \"$dir_name\""

        # Amend the previous commit with the new message
        git commit --amend -m "$message"
        
        # Push the changes to the remote branch
        git push -f
        
        # Go back to the repo directory
        cd .. || continue
    fi
done


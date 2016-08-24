Git Commands
============
Complete the command by 'tab'

::

    git --version                       #Prints the Git suite version

    git config -e		        #edit .git/config
    git config -e --global	        #edit ~/.gitconfig
    git config -e --system	        #edit /etc/gitconfig
    git config a.b	                #get a.b in .git/config
    git config --global a.b something	#set a.b in ~/.gitconfig
    git config --unset a.b 	        #remove a.b

    git add hello.c 		        #Add a single file to stage
    git add doc/\*.txt                  #Add all *.txt file 
    git add -A			        #Add all the modified, deleted and new files
    git add -i			        #Add modified contents in the working tree interactively to the index.
    git add -p [filename]               #equal to -i and then select the patch command
            stage this hunk [y,n,q,a,d,/,s,e?]
               y - stage this hunk
               n - do not stage this hunk
               q - quit; do not stage this hunk nor any of the remaining ones
               a - stage this hunk and all later hunks in the file
               d - do not stage this hunk nor any of the later hunks in the file
               g - select a hunk to go to
               / - search for a hunk matching the given regex
               j - leave this hunk undecided, see next undecided hunk
               J - leave this hunk undecided, see next hunk
               k - leave this hunk undecided, see previous undecided hunk
               K - leave this hunk undecided, see previous hunk
               s - split the current hunk into smaller hunks
               e - manually edit the current hunk
               ? - print help

    git clean -fd		        #Clear all unmanaged files
    git clean -fX                       #Clear all the files defined in .gitignore
    git checkout .		        #Clear all changes to the managed files

    git commit -s	                #Add signoff line automatically, and need to add log message in editor.
    git commit -m "log message"	        #Commit with log message without pop-up editor.
    git commit --amend		        #Update the log message in last commit
    git commit --amend --allow-empty --reset-author   #Update the author in last commit

    git checkout master		        #checkout master branch
    git checkout .		        #clear all the changes to the managed file in workspace
    git checkout -- filename	        #checkout single file
    git checkout branchname -- filename #checkout file in other branch, both stage and workspace will be changed.
    git checkout -b branchname          #create and switch to the new branch

    git reset --soft <commit>	        #reset HEAD refernce, but not the content
    git reset --soft HEAD^		#revert the git commit
    git reset --hard HEAD^		#reset both reference and content changed.
    git reset --hard master@{2}
    git reset [HEAD]		        #revert git add, reset what are not committed.
    git reset HEAD filename		#reset single file in stage

    git clone
    git push
    git pull
    git pull --rebase		        #rebase
    git merge <commit>		        # merge current HEAD and commit
    git cherry-pick <commit>	        #pick commit in any branch and put it after current HEAD
    git revert HEAD		        #revert itself is a commit

    git rebase --autostash              #Stash changes before rebasing

    git grep --line-number "something"  #grep in tracked files

    git status			        #option -s for short version
    git status --ignored                #show the ignored files list at the same time

    git config user.name [value]        #no value means get value, otherwise set the value
    git config --luser.name

    git log --pretty=fuller
    git log --pretty=oneline	        #equal to --oneline
    git log --pretty=raw
    git log --graph --oneline
    git log -p HEAD			#-p is to show the diff patch in each commit
    git log --stat HEAD		        #show what files are changed
    git log --oneline --decorate	#Show all tags and other references
    git log -3
    git log ^HEAD~3 HEAD
    git log HEAD~3..HEAD
    git log --pretty=short --decorate   #Show commit log together with ref names, such as tags.
    git log --format="%h | %s | %d"     #Show log in "Hash | Subject | Ref-names" format
    git log Branch1 ^Branch2            #Show commit which in Branch1 but not in Branch2
    git log --all --grep 'something'    #Show commit log which match the special text.
    git log -- filename                 #Show commit log related to special file.

    git shortlog                        #Show summary only, but grouped by author.

    git cherry -v master                #Show all commits which are not merged to master yet.

    git describe --tags --abbrev=0      #Show the last tag

    git show HEAD --stat
    git show-ref
    git show <branch_name>:<file_name>  #Show file in special branch

    git diff                            #workspace to stage
    git diff --cached                   #stage to remote
    git diff HEAD                       #workspace to remote
    git diff HEAD^ HEAD
    git diff HEAD^ HEAD -- filename     #the diff of single file
    git diff --word-diff                #Show inline changes in detail

    git blame filename
    git blame -L 6 +5 filename	        #only show 5 lines begin from line 6

    git format-patch -1

    git stash			        #store all current changes
    git stash list		        #list all stash
    git stash pop		        #apply and remove the newest stash
    git stash apply		        #only apply but do not remove
    git stash drop [stash]	        #remove the stash, the newest by default
    git stash clear		        #clear all stash

    git branch			        #show local branches
    git branch -r/-a			#show remote/all branches
    git branch branchname <commit>	#create branch based on <commit>, HEAD by default
    git branch -d branchname	        #remove local branch， see also -D
    git branch -m oldbranch newbranch	#rename branch，see also -M
    git push <url>  :remote-branch      #remove remote branch, need to sync back by 'git fetch -p'

    git tag -m "log message" tagname    #create tag
    git tag				#show local tags
    git tag -l V3_*			#show local tags which match the pattern
    git tag -d tagname		        # delete the tag
    git push origin tagname		#push the tag in local
    git describe --tags			#desciption about the last tags

    git remote -v			#show remote URL
    git remote add new-remote path 	#add new remote URL
    git remote rename old-remote new-remote
    git remote rm remotename	        #remove remote
    git remote show origin              #show info about current origin
    git remote update

    git rev-parse --git-dir		#show the path of .git folder of current repository
    git rev-parse --show-toplevel	#show the top direcotry of current repository
    git rev-parse --show-prefix	        #how to go from top directory to current directory
    git rev-parse --show-cdup	        #how to back to top directory (e.g. '../../../')
    git rev-parse HEAD		        #show the commit ID of HEAD
    git rev-parse HEAD^
    git rev-parse --symbolic --branches #show local branches
    git rev-parse --symbolic --tags	#show local tags
    git rev-parse --abbrev-ref HEAD     #Show the name of current branch

    git rev-list --oneline A	        #show the version relationship

    git ls-files -s 		        #show file tree and last commit ID
    git ls-tree -l HEAD
    git ls-files --others -i --exclude-standard  # Show all files which are ignored.

    git cat-file -t <ID>		#type of the ID (commit or tag ...)
    git cat-file -p <ID>		#content of the ID

    git reflog show master	        #show the log on master branch
    git reflog -1			#show last action of HEAD


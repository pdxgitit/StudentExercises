# Intro to GIT

your local repository consists of three "trees" maintained by git.
The first one is your Working Directory which holds the actual files.
The second one is the Index which acts as a staging area and finally
the HEAD which points to the last commit you've made.

You can add files to the Index using:

    **git add <filename>**

(or git add * to add all files | or git add --a to add all files)

This will move files to the staging area.  To actually commit these changes use:

    **git commit -m "commit message"**

Now stages files are committed to the HEAD but not your remote repository yet.

To send those changes to your remote repository use:

    **git push origin master**

origin is a shorthand (or alias) for the url that your repository lives at (remote repo).
(i.e. https://github.com/PDX-Evening-Bootcamp-Nov2015/Repo_name)

master indicates the name of the branch you are pushing to.

If you have not cloned an existing repository and want to connect your repository
to a remote server, you need to add it with:

    **git remote add origin <server>**

Branches are used to keep changes isolated from each other.  Master should never
be worked on directly (especially when working on a team).  Create a branch to make
any changes and then merge those changes into master when complete.

                   _____BRANCH_______
                  /                  \
          ----------------MASTER----------------->

To create a new branch use:

    **git checkout -b <branchname>**

To switch back to master use:

    **git checkout master**

To delete a branch use:

    **git branch -d <branchname>**

Your branch will not be available to others unless you push the branch to the
remote repository (not generally necessary):

    **git push origin <branchname>**

To merge another branch into your current active branch use:

    **git merge branch**

In general you should be on your master branch when using this command!  Sometimes
when you are trying to merge a branch there will be conflicts.  You need to manually
fix the conflicts by editing the files shown by git.  After making these changes you
need to mark them as merged using:

    **git add <filename>**

You can preview the changes you have made before merging by using:

    **git diff <source branch> <target branch>**

To update your local repository to the newest commit use:

    **git pull**

This will "fetch" and "merge" remote changes.

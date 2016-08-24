Git Work Flow
=============

Create Repository
-----------------
Initialize a empty repository::

    git init --bare

Clone a mirror repository， sync via "git remote update/git fetch" later::
    git clone --mirror


Generate git patch outside git repo
-----------------------------------
::

    git init
    git add -A
    git commit -s

    #change some things ...

    git add -A
    git commit -s
    git show

    git format-patch -1


Git flow
--------

http://nvie.com/posts/a-successful-git-branching-model/

Install::

    $ sudo apt-get install git-flow

Usage::

    |         +-- init
    |         |
    |git flow +-- feature --+-- start   --+-- name
    |         |             |             |
    |         +-- release --+-- finish  --+
    |         |             |             |
    |         +-- hotfix  --+-- publish --+
    |                       |             |
    |                     --+-- pull    --+

Details::

    a. create develop branch

    git branch develop
    git push -u origin develop    

    b. Start new feature

    git checkout -b some-feature develop
    # Optionally, push branch to origin:
    git push -u origin some-feature    

    git status
    git add some-file
    git commit    

    c. finish the feature

    git pull origin develop
    git checkout develop
    git merge --no-ff some-feature
    git push origin develop

    git branch -d some-feature

    # If you pushed branch to origin:
    git push origin --delete some-feature    

    d. Start new relase

    git checkout -b release-0.1.0 develop

    # Optional: Bump version number, commit
    # Prepare release, commit

    e. Finish the release

    git checkout master
    git merge --no-ff release-0.1.0
    git push

    git checkout develop
    git merge --no-ff release-0.1.0
    git push

    git branch -d release-0.1.0

    # If you pushed branch to origin:
    git push origin --delete release-0.1.0   


    git tag -a v0.1.0 master
    git push --tags

    f. Start new hotfix

    git checkout -b hotfix-0.1.1 master    

    g. Finish the hotfix

    git checkout master
    git merge --no-ff hotfix-0.1.1
    git push


    git checkout develop
    git merge --no-ff hotfix-0.1.1
    git push

    git branch -d hotfix-0.1.1

    git tag -a v0.1.1 master
    git push --tags


Github Flow
-----------

| https://guides.github.com/introduction/flow/
| http://scottchacon.com/2011/08/31/github-flow.html


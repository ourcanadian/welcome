# Welcome | Bienvenue

This repo was built to help you get familiar with the OurCanadian codebase and github.

## Open your terminal or console in a new directory
Personally on Mac I usually start just by opening the Terminal app and going from there.
```
cd Documents
mkdir ourcanadian
cd ourcanadian
```

## Clone the repo
```
git clone https://github.com/ourcanadian/welcome.git
```

## Run the code
```
cd welcome
python3 guestbook.py
```
You should see a list of names show up, letting you know when those names were put there. We'd like you to have your name in there too.


## Create a branch
Replace `username` with your github username so we know whose branch this is.
```
git checkout -b add-username
```
(e.g. `git checkout -b add-rylancole` so the branch is named `add-rylancole`)

You can check to make sure you're on the right branch now.
```
git branch
```

_Note: Here's how to delete a branch if needed_      
List your local branches and make sure you aren't on the branch you want to delete.
```
git branch
```
A * will mark the branch you are on. If needed, change your branch.
```
git checkout master
```
Delete the branch by replacing `NAME` with the name of the branch you want to delete.
```
git branch -d NAME
```

## Add yourself to the guestbook
Open `guestbook.json` however you please and follow the format to add yourself in at the bottom.
```
{
  "name": "YOUR NAME",
  "github": "YOUR USERNAME",
  "date": "TODAY YYYY-MM-DD"
}
```
Be careful of your commas, json files can be picky. Run the code again to make sure it worked.
```
python3 guestbook.py
```

## Stage and push the changes
Now it's time to lock in those changes so everyone after you will see you in the guestbook.  
Always look first to see what files you changed. You should only see `guestbook.json`
```
git status
```
So we add `guestbook.json` and check to see that worked
```
git add guestbook.json
git status
```
Now we can send those changes. Change `username` again.
```
git commit -m 'username welcome commit'
git push --set-upstream origin add-username
```
If you get 'permission denied' when trying to push it is because you are not a part of the organization. Make sure you have accepted your invitation to join!

## Create a pull request
Go to the [repo on github](https://github.com/ourcanadian/welcome) and you should see a new banner with a button that says "Compare & pull request". Click that to create a pull request, add a comment about why you decided to take a look at this project.

## You're ready to go
Pull requests need to be approved by another user before they can be merged in the main branch. Once that has happened, your name will be in the master guestbook that any new user will fetch when they clone this repo.

## Explore
We have many other projects we are working on, follow their README files to get started wherever you are interested.

[/r/BuyCanadian Wiki Bot - Reddit Wiki Replier](https://github.com/ourcanadian/wiki-replier)

[Our Canadian Wiki API Wrapper - OCWA](https://github.com/ourcanadian/ocwa-wrapper)

[Search Engine UI Proof-Of-Concept - OCSE UI](https://github.com/ourcanadian/ocse-ui-poc)



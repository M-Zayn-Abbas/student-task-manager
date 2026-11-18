# Lab Report: Student Task Manager with Git and GitHub

**Course:** DevOps for Cloud Computing (CSC418)
**Assignment:** Lab Assignment 4
**Student:** M. Zayn Abbas
**Repository:** https://github.com/M-Zayn-Abbas/student-task-manager
**Release:** https://github.com/M-Zayn-Abbas/student-task-manager/releases/tag/v1.0.0

---

## 1. Git vs GitHub; purpose of add, commit and push

**Git** is a version control tool that runs on my own computer. It tracks every change to my files and keeps the full history locally. **GitHub** is an online platform that hosts Git repositories. It adds collaboration features on top of Git, such as Pull Requests, Issues, Actions and Releases, so a team can share and review code.

- `git add` moves changes into the **staging area**, which lets me choose exactly what goes into the next commit.
- `git commit` saves the staged changes as a **snapshot** in local history, with a message that describes the change.
- `git push` uploads my local commits to the **remote repository** on GitHub so others can see them and the history is backed up.

## 2. Why branches and Pull Requests are used; what causes merge conflicts

**Branches** let me build each feature separately without breaking the working code on `main`. In this project, `feature/add-task`, `feature/complete-task` and `feature/delete-task` were developed in parallel, each with its own commits.

**Pull Requests** are a way to review a branch before it is merged. They show the changed files, allow review comments, run the automated tests, and link to the Issue being solved (for example `Closes #1`). Code only reaches `main` after it has been checked.

A **merge conflict** happens when two branches change the **same line of the same file** differently, so Git cannot decide which version to keep. In Part D, both `status-in-progress` and `status-complete` changed the `Project status` line in README.md. After the first branch was merged, merging the second one caused a conflict that I resolved by hand. The unrelated `Author` line from the second branch merged without problems.

## 3. fetch vs pull; merge vs rebase

- `git fetch` downloads new commits from the remote but **does not change** my working files or current branch, so I can inspect them first.
- `git pull` is `fetch` + `merge`: it downloads the commits **and** merges them into my current branch straight away.

- **Merge** combines two branches by creating a **merge commit**. It keeps the real history, including where branches split and joined.
- **Rebase** moves my commits so they sit **on top of** another branch, which gives a straight, linear history. Because it rewrites commits, it should not be used on commits that have already been pushed and shared.

## 4. How GitHub Issues and Actions help a team

**Issues** work as a task list for the project. Each bug, feature or documentation task gets a description and a label (`enhancement`, `bug`, `documentation`), and can be linked to the Pull Request that fixes it, so the team always knows what is planned, in progress or done.

**GitHub Actions** automates checks. My workflow runs all unit tests on every push to `main` and on every Pull Request. In Part E, a deliberately wrong test made the run **fail**, which showed that broken code is caught before merging. After the fix, the run **passed**. This gives the team confidence that `main` always works.

## 5. One difficulty I faced and how I solved it

During the merge conflict in Part D, I committed the merge **before removing all the conflict markers** (`<<<<<<<`, `=======`, `>>>>>>>`), and that commit was pushed. I then used `git commit --amend` to fix it, but because the bad commit was already on GitHub, my local and remote histories split. `git pull` created a second conflict, and some leftover markers were committed again.

**Solution:** I removed the remaining markers and made a normal new commit (`Remove leftover conflict markers from README`) instead of rewriting history with a force push. I learned to:
- check for leftover markers with `git diff --check` before committing a resolution, and
- never amend commits that have already been pushed, and make a new commit instead.

---

## Summary of Work

| Requirement | Evidence |
|---|---|
| Meaningful commits (12+) | 30+ commits in history |
| Feature branches (3) | `feature/add-task`, `feature/complete-task`, `feature/delete-task` |
| Issues (4) | #1 to #4 with labels |
| Merged Pull Requests (5) | #5, #6, #7, #8 and the documentation/report PR |
| Resolved merge conflict (1) | README `Project status` conflict (Part D) |
| Automated tests (3+) | 6 tests in `tests/test_task_manager.py` |
| Workflow (1) | `.github/workflows/tests.yml` |
| Release (1) | `v1.0.0` |

Screenshots of the key steps are in the [`lab-evidence`](lab-evidence/) folder.

# GitHub Workflow Playbook — Upload, Verify, Merge/Replace, Logs

Reference doc, not a skill — paste the relevant section into a session when
you're about to touch a repo, or just read it before you start. Written from
the actual PowerShell + git CLI session that built the TicketingSystem repo,
so the commands below are proven, not theoretical.

Environment assumed: Windows PowerShell, `git` CLI, GitHub remote already
created (empty or non-empty).

---

## 0. Before you touch git — pre-flight checklist

- [ ] Is the thing you're about to commit **extracted**, not a zip? Git can't
      see inside a `.zip` — committing one just stores an opaque blob, not
      your actual files. Extract first, delete the zip after.
- [ ] Are you in the **right folder**? `pwd` (or just look at the prompt —
      PowerShell shows the full path). A `git init` in the wrong folder
      creates a `.git` you'll need to clean up later.
- [ ] Does `git remote -v` already point somewhere? If yes, you don't need
      `git remote add origin` again — that errors with "remote origin
      already exists."
- [ ] Do you know if the **GitHub repo is empty or not**? Check in the
      browser before you push anything. An empty repo = simple push. A
      non-empty repo (even just an auto-generated README) = you WILL hit
      "fetch first" / merge conflicts. See §3.

---

## 1. Uploading fresh content (first push to a repo)

```powershell
# 1. Extract if it's a zip
Expand-Archive -Path .\yourfile.zip -DestinationPath .\extracted

# 2. Move contents to repo root (not nested inside extracted\subfolder\...)
Move-Item .\extracted\<inner-folder-name>\* .\
Remove-Item .\extracted -Recurse

# 3. Delete the zip — never commit it
Remove-Item .\yourfile.zip

# 4. Confirm real files are present, not the zip
dir

# 5. Git init only if this folder has no .git yet
git init

# 6. Point at the remote (skip if git remote -v already shows origin)
git remote add origin https://github.com/ORG/REPO.git

# 7. Stage everything, check what's about to be committed
git add .
git status

# 8. Commit
git commit -m "Initial commit"

# 9. Match GitHub's default branch name
git branch -M main

# 10. Push
git push -u origin main
```

**Common trap:** running `git commit` before `git add` looks like it worked
(no error) but actually prints `nothing added to commit but untracked files
present` — that means **nothing was committed**. Always check the commit
actually landed:

```powershell
git log --oneline
```

If this errors with "does not have any commits yet," your commit never
happened — go back to step 7.

---

## 2. Verify something is *actually* uploaded (don't trust the terminal alone)

Three independent checks — use at least two, since each catches different
failure modes:

| Check | Command | What it confirms |
|---|---|---|
| Local history exists | `git log --oneline` | You committed something, locally |
| Local matches remote | `git status` after a `git fetch` | Whether local is ahead/behind/diverged |
| Remote actually has it | Open `https://github.com/ORG/REPO` in a browser | The push actually reached GitHub — not just "no error locally" |

```powershell
git fetch origin
git status
```

Read the output carefully:
- `Your branch is up to date with 'origin/main'` → confirmed uploaded, nothing pending
- `Your branch is ahead of 'origin/main' by N commits` → committed locally, **not yet pushed**
- `Your branch is behind 'origin/main' by N commits` → remote has things you don't have locally yet
- `Your branch and 'origin/main' have diverged` → both sides have unique commits — this is the merge/replace decision point, go to §3

**Never assume a push worked just because the command returned with no
red text.** Always follow with the browser check for anything that matters.

---

## 3. Deciding: is this a MERGE or a REPLACE situation?

This is the fork in the road that caused the conflict in the TicketingSystem
repo. Figure out which situation you're in **before** running `git pull`.

### You're in a MERGE situation if:
- The remote repo has commits you don't have locally AND
- You want to **keep both** sets of changes (or at least evaluate both)

→ Use `git pull` (see §4). This is the safe default — it never destroys
history, it just might create conflicts you have to resolve by hand.

### You're in a REPLACE situation if:
- The remote has old/wrong/throwaway content (e.g. a stray auto-generated
  README, a broken previous attempt) AND
- Your local copy is the one that should win, entirely, no merging

→ This needs a **force push**, which is destructive to the remote history.
Never do this without checking the remote in a browser first.

```powershell
# DESTRUCTIVE — remote history for this branch is overwritten.
# Only do this if you are certain the remote has nothing worth keeping.
git push --force origin main
```

**Guardrail:** before force-pushing, always run this first so you have a
recovery point if you're wrong:

```powershell
git fetch origin
git branch backup-before-force origin/main
```

That creates a local branch (`backup-before-force`) pointing at whatever
was on the remote, so if the force-push turns out to have destroyed
something you needed, you can still find it locally.

---

## 4. Handling a merge (the non-destructive path)

```powershell
git pull origin main --allow-unrelated-histories
```

`--allow-unrelated-histories` is only needed the *first* time two
independently-initialized repos (yours locally, GitHub's auto-created one)
get connected. After that first successful merge, plain `git pull` is enough.

**If it says "Auto-merging ... CONFLICT (add/add)":**

```powershell
# See exactly which files are still conflicted
git status
```

Open each conflicted file. You'll see:

```
<<<<<<< HEAD
...your local version...
=======
...the remote's version...
>>>>>>> <commit-hash>
```

Decide, per file:

```powershell
# Keep YOUR local version entirely for this file
git checkout --ours path/to/file
git add path/to/file

# Keep the REMOTE's version entirely for this file
git checkout --theirs path/to/file
git add path/to/file

# Or: manually edit the file, delete the <<<<<<< ======= >>>>>>> markers
# yourself, keeping/combining whatever you want, then:
git add path/to/file
```

Once every conflicted file is resolved and staged:

```powershell
git status          # should show "All conflicts fixed" or nothing left unmerged
git commit -m "Merge remote history, resolve conflicts"
git push -u origin main
```

---

## 5. Checking logs — three different meanings

"Check the logs" means three different things depending on what you're
debugging. Don't reach for the wrong one.

### A. Git commit history (what changed, when, by whom)

```powershell
git log --oneline                 # compact, one line per commit
git log -p -- path/to/file        # full diff history for one file
git log --stat                    # which files changed per commit, line counts
git show <commit-hash>            # full detail of one specific commit
```

### B. What's different right now, uncommitted

```powershell
git status                        # what's staged/unstaged/untracked
git diff                          # unstaged changes, line by line
git diff --staged                 # staged changes, line by line
```

### C. Runtime/deploy logs (is the *app* actually working, not just the repo)

This is a different system entirely — git logs tell you nothing about
whether the deployed app is running correctly.

- **Render:** Dashboard → your service → **Logs** tab. Look for the boot
  sequence (`Bootstrap admin created...`, `... listening on port ...`) or
  crash traces.
- **Browser console:** F12 → Console tab. Catches client-side errors (CSP
  violations, failed fetches, JS exceptions) that never show up in Render's
  server logs at all.

**Rule of thumb:** if something looks wrong in the browser, check the
browser console first — git and Render logs won't show a CSP violation or
a JS error, only the server-side half of the picture.

---

## 6. Quick reference — which command when

| Situation | Command |
|---|---|
| "Did I actually commit?" | `git log --oneline` |
| "Did I actually push?" | `git fetch origin && git status` |
| "Is the remote ahead of me?" | `git status` after `git fetch` — look for "behind" |
| "What changed in this file over time?" | `git log -p -- <file>` |
| "What's uncommitted right now?" | `git status` then `git diff` |
| "I want to undo my last commit (not yet pushed)" | `git reset --soft HEAD~1` |
| "I want to undo a commit that's already pushed" | `git revert <commit-hash>` (safe, adds a new commit) — never `git reset` on shared history |
| "Remote has junk I don't want, mine should win" | See §3 REPLACE path — force push, with a backup branch first |
| "Remote and I both have real changes to keep" | See §4 MERGE path |

---

## 7. Pitfalls actually hit (keep growing this list)

| Symptom | Root cause | Fix |
|---|---|---|
| `git commit` succeeds with no error but nothing is committed | Forgot `git add` first | Always `git add .` then `git status` before `git commit` |
| `git push` rejected: "fetch first" | Remote has commits (e.g. auto-created README) that local doesn't | `git pull origin main --allow-unrelated-histories` |
| `CONFLICT (add/add)` after pulling | Same filename exists on both sides with different content | Resolve per-file with `--ours`/`--theirs`/manual edit (§4) |
| PowerShell PSReadLine crash scrolling command history | Terminal buffer/rendering bug in old PSReadLine version, not a git problem | Close and reopen the terminal; avoid mashing UpArrow repeatedly |
| Pushed a `.zip` instead of the actual files | Skipped extraction | Extract first, delete zip, re-add real files, re-commit |
| Admin login works locally but not on Render | Wrong env var name (e.g. `ADMIN_PASSWORD` vs the app's actual `ADMIN_BOOTSTRAP_PASSWORD`) | Check the app's `config/index.js` or README for the *exact* env var names it reads — don't assume names carry over between projects |
| App "not loading" with no visible error | Unhandled promise rejection before `app.listen()` — server never bound a port | Add `.catch()` on any async boot step so the server starts listening even if setup logic fails, and logs the failure instead of hanging silently |
| Browser console: "Executing inline script violates CSP" | An inline `<script>...</script>` block in an HTML file, while the server's Content-Security-Policy only allows `'self'` | Move the script into an external `.js` file and reference it with `<script src="...">` |

---

## 8. Emergency rollback

```powershell
# Undo the last commit, keep the file changes staged (safe, local-only, not yet pushed)
git reset --soft HEAD~1

# Undo the last commit AND discard the file changes entirely (DESTRUCTIVE, local-only)
git reset --hard HEAD~1

# Undo a commit that's ALREADY on GitHub — never rewrite shared history,
# add a new commit that reverses it instead
git revert <commit-hash>
git push origin main
```

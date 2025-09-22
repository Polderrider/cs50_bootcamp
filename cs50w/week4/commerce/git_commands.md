
 ┌─────────────────────────┐
 │ Start work (day)        │
 │   git checkout main     │
 │   git pull origin main  │   ← ensure local main is up to date
 └──────────┬──────────────┘
            │
            ▼
┌─────────────────────────────────┐
 │ Create new feature              │
 │   git checkout -b feature/XX-...  │
 │   git push -u origin feature/XX-  │
 └──────────┬──────────────────────┘
            │
            ▼
 ┌───────────────────────┐
 │ Work on feature       │
 │   git add .             │
 │   git commit -m "..."   │
 │   git push              │
 └──────────┬────────────┘
            │
            ▼
 ┌──────────────────────────────┐
 │ Keep feature in sync        │
 │   git rebase origin/main      │   ← (before PR if main has moved)
 │   git push --force-with-lease │
 └──────────┬───────────────────┘
            │
            ▼
 ┌───────────────────────┐
 │ Open PR on GitHub      │
 │ Review & Merge → main  │
 └──────────┬────────────┘
            │
            ▼
 ┌───────────────────────┐
 │ After PR merged        │
 │   git checkout main       │
 │   git pull origin main    │  ← sync local main again
 └──────────┬────────────┘
            │
            ▼
 ┌───────────────────────┐
 │ Ready for next feature │
 └───────────────────────┘



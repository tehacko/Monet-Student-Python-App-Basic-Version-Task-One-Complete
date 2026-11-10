# Fat Burner — minimum CML version

Same layered structure as the extended app, reduced to the original minimum lesson:

- users: `name`, `weight`, `reference` only
- stats: calorie maintenance level (CML) only
- no skinfolds / age / body-fat calculations

## Layers

| Layer | File |
|---|---|
| Controller | `frontend_controller.py` |
| Service | `service.py` |
| Repository | `repository.py` |
| Entry | `main.py` |

## Run

From this folder:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Put the service account JSON next to `repository.py` and set `SERVICE_ACCOUNT_FILE` / `SHEET_NAME` there.

Saved sheet rows are: `date`, `weight`, `cml`.

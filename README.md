<div align="center">

# ChronoVault

### A simple, self-defending Python file vault

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](#requirements)
[![Dependencies](https://img.shields.io/badge/Dependencies-None-2E7D6B?style=for-the-badge)](#requirements)
[![License](https://img.shields.io/badge/License-MIT-EFB06B?style=for-the-badge)](#license)

</div>

---

## Overview

ChronoVault is a simple yet effective Python-based file vault that protects your directory contents. After **3 failed password attempts**, the vault locks itself for **12 hours**, preventing any further access until the lock expires.

## Features

| Feature | Description |
|---|---|
| Password-protected access | Only the correct password unlocks the vault |
| 12-hour lockout | Triggers automatically after 3 failed attempts |
| Auto-display of files | Shows all directory contents (excluding the script) once unlocked |
| Event logging | Access attempts logged to `vault_access` |
| Lightweight | No external dependencies |

## How It Works

1. Run the script.
2. Enter the correct password (`heybaby` by default).
3. If the wrong password is entered 3 times, the vault locks for 12 hours.
4. Once the lockout expires, the vault can be accessed again.

```
Attempt 1 ❌  →  Attempt 2 ❌  →  Attempt 3 ❌  →  🔒 Locked for 12 hours
```

## Files

| File | Purpose |
|---|---|
| `vault.py` | Main script |
| `vault.lock` | Lock file (auto-created after failed attempts) |
| `vault_access` | Log of access events |

## Requirements

- Python 3.x
- `os` module (standard library)
- `time`, `datetime`, `logging` modules (standard library)

No installation needed beyond a standard Python 3 environment — just run the script.

```bash
python vault.py
```

## Note

For educational purposes only. Modify and expand it to suit your needs.

## License

MIT License

---

<div align="center">
<sub>Built by Khadija Bilal.</sub>
</div>

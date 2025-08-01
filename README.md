
# ChronoVault 🔐

ChronoVault is a simple yet effective Python-based file vault that protects your directory contents. After 3 failed password attempts, the vault locks itself for 12 hours, preventing any further access until the lock expires.

## 🔧 Features

- 🔐 Password-protected access
- ⏳ 12-hour lockout after 3 failed attempts
- 📁 Auto-display of all files (excluding script) upon correct password
- 📝 Logging of events to `vault_access`
- 📦 Lightweight, no external dependencies

## 🚀 How It Works

1. Run the script.
2. Enter the correct password (`heybaby` by default).
3. If incorrect password is entered 3 times, vault locks for 12 hours.
4. After time expires, the vault can be accessed again.

## 📄 Files

- `vault.py` - Main script
- `vault.lock` - Lock file (auto-created after failed attempts)
- `vault_access`  - Log files

## 📌 Note

For educational purposes only. Modify and expand it to suit your needs.

## 🛠 Requirements

- Python 3.x
- OS module (standard)
- Time, datetime, logging modules (standard)

## 📜 License

MIT License

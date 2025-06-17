# 🗨️ OpenChatSpace

A simple cross-platform (Linux, Termux, Windows) chat application using Python and MongoDB. Works entirely through the command line — no external libraries for UI or web frameworks.

---

## 📂 Project Structure

```
chat_app/
├── config.py              # MongoDB connection settings
├── core.py                # Shared message logic (send/receive)
├── chat.py                # Launcher
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🔧 Requirements

- Python 3.x
- MongoDB (local or remote)
- `pymongo` library

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ MongoDB Setup

### Option 1: Local MongoDB Server

Ensure MongoDB is installed and running on:

```
mongodb://localhost:27017/
```

### Option 2: Remote MongoDB Server (Termux Users)

If you're on Termux or a system that doesn't support MongoDB:
- Run MongoDB on another machine (Linux/Windows/Cloud)
- Update the connection URI in `config.py`:

```python
client = MongoClient("mongodb://<IP_ADDRESS>:27017/")
```

Make sure the firewall allows connections to port `27017`.

---

## 🚀 Usage Instructions

### Launch Terminal
```bash
python chat.py
```

Once launched:
- Enter a username
- Start chatting!
- Type `/exit` to leave the chat

---

## 📦 Features

- Cross-platform support (Termux, Linux, Windows)
- Real-time message viewing (polling-based)
- Uses only Python and MongoDB
- No need for servers or frameworks

---

## 💡 Roadmap / Ideas

- Add chat rooms or channels
- Add file/image sharing (base64 encoded)
- Improve message syncing using WebSockets
- Add GUI (Tkinter, PyQt, or Electron)
- Add username registration and password support

---

## 🛠️ Troubleshooting

- **MongoDB not connecting?** Make sure the database is running and accessible at the given URI.
- **Duplicate messages?** Avoid using the same username across terminals.
- **On Termux?** Use remote MongoDB — local MongoDB isn't supported without heavy workarounds.

---

## 📜 License

MIT License. Free to use, modify, and distribute.

---

## 🙋‍♂️ Credits

Built with ❤️ using:
- Python
- MongoDB
- Terminal Aura 😎

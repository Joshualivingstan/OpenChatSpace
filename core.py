import time
import threading
from datetime import datetime
from pymongo import MongoClient
from prompt_toolkit import prompt
from prompt_toolkit.patch_stdout import patch_stdout
from config import messages_collection

def send_message(username):
    while True:
        try:
            with patch_stdout():
                msg = prompt(f"[{datetime.utcnow().strftime('%H:%M:%S')}] {username}: ")
            if msg.lower() == "/exit":
                print("Leaving chat...")
                break
            elif msg.lower() == "/help":
                print("/user - shows your username \n/exit - exits the chat\n/help - displays commands and description")
                continue
            elif msg.lower() == "/user":
                print(f"Your username: {username}")
                continue
            messages_collection.insert_one({
                "username": username,
                "message": msg,
                "timestamp": datetime.utcnow()
            })
        except KeyboardInterrupt:
            print("\nExiting...")
            break

def receive_messages(username):
    last_seen_time = datetime.utcnow()
    while True:
        new_msgs = messages_collection.find({
            "timestamp": {"$gt": last_seen_time}
        }).sort("timestamp")
        for msg in new_msgs:
            if msg["username"] != username:
                ts = msg["timestamp"].strftime("%H:%M:%S")
                print(f"[{ts}] {msg['username']}: {msg['message']}")
            last_seen_time = msg["timestamp"]
        time.sleep(1)

def start_chat(platform_name):
    print(f"=== Chat App [{platform_name}] ===")
    username = input("Enter your username: ")
    print("(type /help to see commands)")
    threading.Thread(target=receive_messages, args=(username,), daemon=True).start()
    send_message(username)

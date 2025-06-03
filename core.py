import time
import threading
from datetime import datetime
from config import messages_collection

def send_message(username):
    while True:
        try:
            msg = input()
            if msg.lower() == "/exit":
                print("Leaving chat...")
                break
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
    print("Type your message (type /exit to leave):")
    threading.Thread(target=receive_messages, args=(username,), daemon=True).start()
    send_message(username)

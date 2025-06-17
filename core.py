import time
import threading
import socket
from datetime import datetime
from config import messages_collection
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

def send_message(username):
    while True:
        try:
            msg = input(f"[{datetime.utcnow().strftime('%H:%M:%S')}] {username}: ")
            if msg.lower() == "/exit":
                print("Leaving chat...")
                break
            if msg.lower() ==  "/help":
                print("/user - shows your username \n/exit - exits the chat\n/help - displays commands and description")
            if msg.lower() == "/user":
                pass
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

def get_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def register():
    ip = get_ip()
    if messages_collection.find_one({"_id": ip}):
        return False
    try:
        messages_collection.insert_one({"_id": ip})
        return True
    except DuplicateKeyError:
        return False

def unregister_device_by_ip():
    ip = get_ip()
    messages_collection.delete_one({"_id": ip})
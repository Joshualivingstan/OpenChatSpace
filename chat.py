from core import start_chat

def mode_sel():
  mode = input("Platoform:  (Termux - T/Linux - L/Windows - W) > ")
  if mode.capitalize() == 'L':
    start_chat("Linux")
  elif mode.capitalize() == 'T':
    start_chat("Termux")
  elif mode.capitalize() == 'W':
    start_chat("Windows")
  else:
    print("Invalid! Select one of the listed platforms!")\
    mode_sel()

if __name__ == "__main__":
  mode_sel()

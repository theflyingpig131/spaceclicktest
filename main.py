import time, os, json, hstesting
global clicks
clicks = 0

#yeah but I beat some of those
#why doesnt that show up

# idk ask elliott


# there now it only shows top 10



def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
def namecheck():
  global clicks
  na = open("attempts.json", "r").read()
  na = json.loads(na)
  nhsh = input("Name: ")
  if nhsh == "":
    clear()
    namecheck()
  else:
    an = {
        "Name":nhsh,
        "Score":clicks
      }
    na.append(an)
  
    na = json.dumps(na, indent=4)
    with open("attempts.json", "w") as f:
      f.write(na)
      f.close()



def timecheck():
  end = time.time()
  check = end - start
  average = clicks / check
  if average > 25:
    quit("CHEATER - John F Kennedy 2025")
  if check > 10:
    clear()
    print("Time up!")
    print("You Clicked " + str(clicks) + " Times!")
    print("You clicked " + str(average) + " Per Second!")
    time.sleep(3)



    namecheck()
    quit()
  elif check <= 10:
    print(check)
def click():
  global clicks
  print("Total Clicks - " + str(clicks))
  input("Press Enter! ")
  clear()
  timecheck()
  clicks = clicks + 1

  click()


print("1) Play")
print("2) Check High Score")
def start_up():
  with open("donk.py","w") as f:
    f.write(os.getenv("code"))
    f.close()
  import donk
  donk.main()
choice = input(": ")
start_up()
if choice == "1":
  clear()
  input("Start? ")
  start = time.time()
  click()
elif choice == "2":
  clear()
  print("====| Leaderboard |====")
  print("Place | Name | Score")
  hstesting.main()

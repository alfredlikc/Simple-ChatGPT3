import openai, getpass, time
from colorama import Fore

############ GLOBAL VARIABLES #############
openai.api_key = "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"
users = {"alfredlikc": "Cans1974", "rian": "12100F", "christoph": "gtx1650", "ay": "laptopsbad", "M": "pentiumFTW"}



############## FUNCTIONS ###############

# login
def loginPrompt():

  # username entry
  usernameEntry = ""
  while usernameEntry not in users.keys():
    usernameEntry = input("Username entry: ")
  
  print()
  
  # password entry
  passwordEntry = ""
  while passwordEntry != users[usernameEntry]:
    passwordEntry = getpass.getpass("Password entry: ")

  return usernameEntry


# chatgpt response generation
def generateResponse(prompt):
  completion = openai.Completion.create(
      engine = "text-davinci-003",
      prompt = prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5
  )
  return completion

# greeting with time
def generateGreeting():
  hour = time.localtime().tm_hour
  if hour in range(3, 12):
    return("morning")
  elif hour in range(12, 17):
    return("afternoon")
  elif hour in range(17, 21):
    return("evening")
  else:
    return("night")

############### MAIN PROGRAM ###############

print(f"{Fore.GREEN}Welcome to Alfred's ChatGPT bot! Please {Fore.RED}login.\n{Fore.RESET}")

loggedIn = loginPrompt()

print(f"{Fore.MAGENTA}\nGood {generateGreeting()}, {loggedIn}!{Fore.RESET}")

while True:
  print(f"\n{Fore.BLUE}----------------------{Fore.RESET}")
  myPrompt = input("\nPlease enter your prompt:\n")

  response = generateResponse(myPrompt).choices[0].text

  print(response)
  print()
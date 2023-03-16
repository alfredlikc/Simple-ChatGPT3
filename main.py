import openai, getpass, time
from colorama import Fore
import passwordHandler

############ GLOBAL VARIABLES #############
openai.api_key = "ADD YOUR OWN API KEY"


############## FUNCTIONS ###############

# login
def loginPrompt():
  username = ""
  while True:
    loggedIn, username = passwordHandler.loginCheck()
    if loggedIn == True:
      return True, username
    print(f"{Fore.RED}Incorrect username or password. Please retry.{Fore.RESET}\n")


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

loggedInUser = loginPrompt()[1]

print(f"{Fore.MAGENTA}\nGood {generateGreeting()}, {loggedInUser}!{Fore.RESET}")

while True:
  print(f"\n{Fore.BLUE}----------------------{Fore.RESET}")
  myPrompt = input("\nPlease enter your prompt:\n")

  response = generateResponse(myPrompt).choices[0].text

  print(response)
  print()
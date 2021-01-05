import random
def Script():
   print("Keep it logically awesome.")

   f = open("quotes.txt")
   quotes = f.readlines()
   f.close()

   end = 13
   rnd = random.randint(0,end)
   print(quotes[rnd])

if __name__== "__main__":
  Script()

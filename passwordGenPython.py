import random

characters= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k',
          'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O',
          'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','@', '#', '$',
          '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')']

char1 = characters[random.randint(0,75)]
char2 = characters[random.randint(0,75)]
char3 = characters[random.randint(0,75)]
char4 = characters[random.randint(0,75)]
char5 = characters[random.randint(0,75)]
char6 = characters[random.randint(0,75)]
char7 = characters[random.randint(0,75)]
char8 = characters[random.randint(0,75)]
char9 = characters[random.randint(0,75)]
char10 = characters[random.randint(0,75)]


print(str(char1)+str(char2)+str(char3)+str(char4)+str(char5)+str(char6)
      +str(char7)+str(char8)+str(char9)+str(char10))

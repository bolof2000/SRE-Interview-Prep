import re
string = "bolofinde . olusegun vic % $ _ test regex "
print(re.sub('\W+','',string).split(" "))
print(re.sub("[^A-Za-z]","",string).split(" "))
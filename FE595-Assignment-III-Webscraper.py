# import request and lxml packages which are used to 
# send a request to theyfightcrime.org to extrct the text
# etree is used to parse the html and get the required content
import requests
from lxml import etree

# Save the male and fermale characters in seperate text ﬁles
# function to extract characters
def exractcharacter():
    #opening male and female files with seperate handlers.
    with open("malecharacter.txt","w") as maleFile, open('femalecharacter.txt', 'w') as femaleFile:   
        for i in range(0,50):
                response = requests.get("https://theyfightcrime.org/") 
                rootelement= etree.HTML(response.content)
                words = rootelement.xpath("//p//text()")
                if(len(words)> 1):
                    characters = words[1]    
                gender = characters.split('She')                  
                if(len(gender)>1):
                    male =gender[0]
                    maleFile.writelines(male+'\n')
                    female = 'she'+gender[1] 
                    femaleFile.writelines(female+'\n')
                elif len(gender) == 0:
                    male =gender[0] 
                    maleFile.writelines(male+'\n')
  
#function call                  
exractcharacter();
                    
                   

                
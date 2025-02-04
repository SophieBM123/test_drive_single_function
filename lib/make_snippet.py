

def make_snippet(str):
    #split string into seperate words
    new_str = str.split(" ")
    #check string is more than 5 words long
    if len(new_str) > 5:
        #get 1st five words and make into a new string
        first_five = new_str[:5]
        snippet = " ".join(first_five) 
        #add '...' and return
        return snippet + '...'
    #return string as is if less than 5 words
    else:
        return str

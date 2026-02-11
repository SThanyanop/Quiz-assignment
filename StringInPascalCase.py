def StringInPascalCase(sentence):
    #Define prefix if it digit at first of the sentence it space onc time only until it not chain wiht digit
    preDigit = False

    #Define Result as the first letter or digit of sentence because at first did nit do any space
    Result = sentence[0]

    #Check if fisrt is digit it can cause misspace when do boolean statement
    if sentence[0].isdigit():
        preDigit = True

    #Loop traverse fron second to the end of letter in sentence
    for i in range(1, len(sentence)):
        
        #If it a alphabet and uppercase will add space and follow by current letter
        if sentence[i].isupper():
            Result += " " + sentence[i]
            
        #If it digit first it will check if previous letter was digit by check predigit, if true no need to space else space then preDigit = true
        elif sentence[i].isdigit():
            if not preDigit:
                Result += " "
                preDigit = True
            Result += sentence[i]
            
        #Normal case
        else:
            Result += sentence[i]

    return Result


sentence = "CHEESECake012345"

print(StringInPascalCase(sentence))

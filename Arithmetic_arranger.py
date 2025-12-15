problems = ["3 + 855", "988 + 40"]

def arithmetic(problems, show_answers = False):
    top_operands = []
    low_operands = []
    operator = []
    
    if len(problems) > 5 :
        return "Error: Too many problems."

    for prob in problems:
        first_add = ""
        sec_add = ""
        # space_index determines the index of the first space character per element of problems list
        space_index = prob.index(" ")
        operator.append(prob[space_index + 1])
        
        # will append each sign to the operators list per element of problems list
        if prob[space_index + 1] != "+" and prob[space_index + 1] != "-":
            return "Error: Operator must be '+' or '-'."

        for y in range(len(prob)):
            # will append to top_operands list all strings before the index character per element of problems list
            if y < space_index:
                first_add += prob[y]
                
            # will append to low_operands list all strings after the second space character per element of problems list   
            if y > space_index and prob[y] != " " and prob[y] != "+" and prob[y] != "-":
                sec_add += prob[y]
        top_operands.append(first_add)
        low_operands.append(sec_add)

    numbers = ['0','1','2','3','4','5','6','7','8','9']
    for el in top_operands:
        for m in range(len(el)):
            if el[m] in numbers:
                continue
            else:
                return 'Error: Numbers must only contain digits.'
    for em in low_operands:
        for n in range(len(em)):
            if em[n] in numbers:
                continue
            else:
                return 'Error: Numbers must only contain digits.'
        
        
    """ This part of the code creates three lists: top_row, mid_row, low_row. In each respective list, we will append all the strings that are gonna / 
        be printed out for each element of the lists (including spaces, e.g.: ' 32    ' first element of top_row, "+  8    " firs element of mid_row, /
        and "----" which has the length of the longer element plus two, from each addition or subtraction.  )
    """  
    
    total = []
    z = 0
    top_row = []
    mid_row = []
    low_row = []
    while z < len(problems):
        if len(top_operands[z]) > 4 or len(low_operands[z]) > 4:
            return "Error: Numbers cannot be more than four digits." 
        if len(top_operands[z]) > len(low_operands[z]) and z <= len(problems) - 2:
            char_top = " "*2 + top_operands[z] + " "*4
            char_mid = operator[z] + " " + " "*(len(top_operands[z])-len(low_operands[z])) + low_operands[z] + " "*4
            char_low = "-"*(len(top_operands[z])+2) + " "*4 
            top_row.append(char_top)
            mid_row.append(char_mid)
            low_row.append(char_low)
        elif len(top_operands[z]) > len(low_operands[z]) and z == len(problems) - 1:
            char_top = " "*2 + top_operands[z]
            char_mid = operator[z] + " " + " "*(len(top_operands[z])-len(low_operands[z])) + low_operands[z]
            char_low = "-"*(len(top_operands[z])+2)
            top_row.append(char_top)
            mid_row.append(char_mid)
            low_row.append(char_low)
                
        if len(top_operands[z]) < len(low_operands[z]) and z <= len(problems) - 2:
            char_top = " "*2 + " "*(len(low_operands[z])-len(top_operands[z])) + top_operands[z] + " "*4
            char_mid = operator[z] + " " + low_operands[z] + " "*4
            char_low = "-"*(len(low_operands[z])+2) + " "*4
            top_row.append(char_top)
            mid_row.append(char_mid)
            low_row.append(char_low)
        elif len(top_operands[z]) < len(low_operands[z]) and z == len(problems) - 1:
            char_top = " "*2 + " "*(len(low_operands[z])-len(top_operands[z])) + top_operands[z]
            char_mid = operator[z] + " " + low_operands[z]
            char_low = "-"*(len(low_operands[z])+2)
            top_row.append(char_top)
            mid_row.append(char_mid)
            low_row.append(char_low)
                
        if len(top_operands[z]) == len(low_operands[z]) and z <= len(problems) - 2:
            char_top = " "*2 + top_operands[z] + " "*4
            char_mid = operator[z] + " " + low_operands[z] + " "*4
            char_low = "-"*(len(low_operands[z])+2) + " "*4
            top_row.append(char_top)
            mid_row.append(char_mid)
            low_row.append(char_low)
        elif len(top_operands[z]) == len(low_operands[z]) and z == len(problems) - 1:
            char_top = " "*2 + top_operands[z]
            char_mid = operator[z] + " " + low_operands[z]
            char_low = "-"*(len(low_operands[z])+2)
            top_row.append(char_top)
            mid_row.append(char_mid)
            low_row.append(char_low)     
        z += 1   
        
    first_row = "".join(top_row)
    sec_row = "".join(mid_row)
    third_row = "".join(low_row)
    problems_list = [first_row,sec_row,third_row]
    pre_problems = "\n".join(problems_list)
    
    if show_answers == False:
        problems = pre_problems
        return problems
    elif show_answers == True:
        total = [str(int(top_operands[cd]) + int(low_operands[cd])) if operator[cd] == "+" else str(int(top_operands[cd]) - int(low_operands[cd])) 
                 for cd in range(len(problems))] 
        total = [" "*(len(low_row[k]) - len(total[k]) - 4) + total[k] + " "*4 if k <= len(problems) - 2 else " "*(len(low_row[k]) - len(total[k])) + total[k] 
                 for k in range(len(total))]
        respuestas = "".join(total)
        problems_list = [first_row,sec_row,third_row,respuestas]
        problems = "\n".join(problems_list)
        return problems
        
    # with any other second argument for the arithmetic function, an error will be raised
    else:
        return "Error: Second argument for arithmatic function is not valid."

    
print(arithmetic(problems, True))
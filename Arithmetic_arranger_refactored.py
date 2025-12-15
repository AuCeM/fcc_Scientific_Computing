problems = ["3 + 855", "988 + 40"]

def arithmetic_solver(probs, show_ans = False):
    split_probs = []
    solutions = []
    str_list = []
    
    top = ''
    mid = ''
    dashes = ''
    sol = ''
    final_str = ''
    
    if len(probs) > 5:
        return "Error: Too many problems."

    for p in probs:
        split_probs.append(p.split(" "))

    for k in split_probs:
        if len(k[0]) > 4 or len(k[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if k[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not k[0].isdigit() or not k[2].isdigit():
            return "Error: Numbers must only contain digits."    
        else:
            if k[1] == "+":
                solutions.append(str(int(k[0]) + int(k[2])))
            else:
                solutions.append(str(int(k[0]) - int(k[2])))


    for m in split_probs:
            if m != split_probs[-1]:
                top += f"  {m[0].rjust(len(m[2]))}    "
                mid += f"{m[1]} {m[2].rjust(1)}    "
                dashes += f"{'-'*(2+len(m[2]))}    "
            else:
                top += f"  {m[0].rjust(len(m[2]))}" + '\n'
                mid += f"{m[1]} {m[2].rjust(5 - len(m[2]))}" + '\n'
                dashes += f"{'-'*(5)}"

    for n in solutions:
        if len(n) == 3 and solutions[-1] != n: 
            sol += f"  {n}    "
        elif len(n) == 3 and solutions[-1] == n:
            sol += f"  {n}"
        elif len(n) == 4 and solutions[-1] != n:
            sol += f" {n}    "
        elif len(n) == 4 and solutions[-1] == n:
            sol += f" {n}"
                
    for _ in [top, mid, dashes, sol]:
        str_list.append(_)

    if show_ans not in [True, False]:
        return "Error: Second argument for arithmetic function is not valid."

    elif not show_ans:
        for f in str_list[:-1]:
            final_str += "".join(f) 

    else:
        for f in str_list:
            if f == sol:
                final_str += '\n' + "".join(f)
            else: 
                final_str += "".join(f)
    
    return final_str



print(arithmetic_solver(problems, 1))
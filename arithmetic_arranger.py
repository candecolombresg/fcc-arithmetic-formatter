import re

def arithmetic_arranger(lista, result=False):
    if len(lista)>5:
        return "Error: Too many problems."
    lista_split = []
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    for problem in lista:
        lista_split.append(re.split("\s",problem))

    for nums in lista_split:
        
        #ERRORES
        if nums[1]!="+" and nums[1]!="-":
            return "Error: Operator must be '+' or '-'."
        if re.findall('[^0-9]',nums[0]) or re.findall('[^0-9]',nums[2]) :
            return "Error: Numbers must only contain digits."
        if len(nums[0])>4 or len(nums[2])>4:
            return "Error: Numbers cannot be more than four digits."

        n = int(max([len(nums[0]),len(nums[2])])+1)
        first_line += nums[0].rjust(n+1)+"    "
        second_line += nums[1] + nums[2].rjust(n) + "    "
        third_line += "-"*(n+1) + "    "
        if result is True:
            if nums[1]=="+":
                fourth_line+= str(int(nums[0])+int(nums[2])).rjust(n+1)+ "    "
            else:
                fourth_line+= str(int(nums[0])-int(nums[2])).rjust(n+1)+ "    "  
    if result is True:
        arranged_problems = first_line.rstrip() +"\n"+ second_line.rstrip() +"\n"+ third_line.rstrip() +"\n"+ fourth_line.rstrip()
    else:
        arranged_problems = first_line.rstrip() +"\n"+ second_line.rstrip() +"\n"+ third_line.rstrip()
    return arranged_problems
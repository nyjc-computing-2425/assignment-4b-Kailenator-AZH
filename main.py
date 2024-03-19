stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()
if all([i in "0123456789xE.^-" for i in stdform]) and stdform.count('.')<=1 and stdform.count('x')<=1 and stdform.count('^')<=1:
  stdform = stdform.replace("x10^","E")
  print("This number in E notation is "+stdform+".")
else:
  print("Error converting to scientific E notation.")
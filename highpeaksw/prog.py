def goodie_dist(goodies_dict,Number_of_employees):  
  goodies_dict_sort = sorted(goodies_dict.items(), key=lambda x: x[1], reverse=False)
  goodies_list=list(goodies_dict.values())
  goodies_list.sort()
  num=Number_of_employees-1
  min=1000000000000000000
  n=len(goodies_list)
  i_val=0
  for i in  range(n-num):
    val=  goodies_list[i+num]-goodies_list[i]
    if val<min:
      min=val
      i_val=i
  
  return goodies_dict_sort,i_val,min
def creat_dict(path):
  #path="/content/input2.txt"
  f = open(path, "r")
  #f_contents = f.read()
  #print(f_contents)
  content = f.readlines() 
  
  # Varaible for storing the sum 
  goody=[]  
  # Iterating through the content 
  # Of the file 
  for line in content: 
    a=[]
    val=0
    for i in line: 
        # Checking for the digit in  
        # the string 
        if i.isdigit() == True:  
            a.append(int(i))
            #print(a)
    if len(a)!=0:
      i=0
      while (i<len(a)-1):
        val+=a[i]*(10**(len(a)-i-1))
        i+=1
      val+=a[i]
    #print(val)
    goody.append(val)
  f.close()
  Number_of_employees=goody[0]
  goody.remove(goody[0])
  goody.remove(0)
  goody.remove(0)
  goody.remove(0)
  with open(path) as myFile:
    text = myFile.read()
    result = text.split('\n')
    i=0
    while(i<len(result)):
      if i<1 or i==len(result)-1:
        result.remove(result[i])
      else:
        split_string = result[i].split(":",1)

        result[i] = split_string[0]
      i+=1
  result.remove(result[0])
  result.remove('')
  result.remove('')
  d = dict(zip(result, goody))
  return d,Number_of_employees
def output(path,goodies_dict,Number_of_employees):
  fd = open(path, 'a')
  goodies_dict_sort,i_val,min=goodie_dist(goodies_dict,Number_of_employees)
  print(Number_of_employees)
  i=i_val

  fd.write("The goodies selected for distribution are:\n\n")
  while i<Number_of_employees+i_val:
    fd.write(str(goodies_dict_sort[i]))
    fd.write("\n")

    i+=1
  fd.write("\n\nAnd the difference between the chosen goodie with highest price and the lowest price is ")
  fd.write(str(min))
  fd.write("\n")

if __name__=="__main__":

  path="/content/sample_input.txt"
  d,Number_of_employees=creat_dict(path)
  pat="/content/p1.txt"
  output(pat,d,Number_of_employees)

  path="/content/input1.txt"
  d,Number_of_employees=creat_dict(path)
  pat="/content/p3.txt"
  output(pat,d,Number_of_employees)

  path="/content/input2.txt"
  d,Number_of_employees=creat_dict(path)
  pat="/content/p2.txt"
  output(pat,d,Number_of_employees)


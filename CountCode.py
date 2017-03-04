def count_code(str):
  count =0
  i = 0
  while "co" in str[i:]:

    if str[i:i+2] == "co" and (i+4 < len(str)+1) and str[i+3] == "e":
      count += 1
    i+=1
  return count

def main():
    print (count_code("codexxcode"))

main()
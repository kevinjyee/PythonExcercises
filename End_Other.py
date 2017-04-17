def end_other(a, b):
  alower = a.lower()
  blower = b.lower()
  if(len(a) > len(b)):
    longer = alower;
    shorter = blower;
  else:
    longer = blower;
    shorter = alower

  print (longer[-len(shorter):]);
  print (shorter);
  return longer[:-len(shorter)] == shorter

def main():
    print(str(end_other("hiabc","abc")));

main()
#!/usr/bin/python3

import random

def main():

  print("coin-toss")
  face=random.randint(0,1)

  if face==0 :
    return "Head"
  else:
    return "Tail"

    
print(main());

def testmain():
  head=0
  tail=0
  # HeadかTainのいずれかが実行されることを確認します。
  for i in 0..9999:
    result=main();
    if result == "Head":
      head++
    else if result == "Tail":
      tail++
    else:
      assert false
  assert  head < 5100
  assert  tail < 5100

  

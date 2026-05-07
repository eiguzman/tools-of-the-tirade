def MainFunc():
  a = 1
  b = 2
  for i in range(5):
    if i == a or i == b:
      print("YES")
    else:
      print("NO")
  return("Done")

if __name__ == "__main__":
    MainFunc()

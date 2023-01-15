def R(n):
  n2 = bin(n)[2:]
  if n2.count("1")%2 == 0:
    n2="10" + n2[2:] + "0"
  else:
    n2="11" + n2[2:] + "1"
  return int(n2, 2)

def print_minimal(min_value):
    for n in range(1, 100):
      if R(n) > min_value:
        print(n)
        break

if __name__ == "__main__":
  print_minimal(16)

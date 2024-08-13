from collections import List

fn contain[type: DType](list: List[Scalar[type]], x: Scalar[type]) -> Bool:
  for e in list:
    if e[] == x:
      return True
  return False

fn unique[type: DType](list: List[Scalar[type]]) -> List[Scalar[type]]:
  var result = List[Scalar[type]]()

  for e in list:
    if not contain(result, e[]):
      result.append(e[])

  return result 

fn print_list[type: DType](list: List[Scalar[type]], sep: String = " ,", end: String = "\n") -> None:

  var length: Int = len(list)

  print("[", end="")

  for idx in range(length - 1):
    print(list[idx], end=sep)
  print(list[length - 1], end='')

  print("]", end="")

  print(end=end)

fn list_count[type: DType](list: List[Scalar[type]], value: Scalar[type]) -> Int64:

  var counter: Int64 = 0

  for e in list:
    if e[] == value:
      counter += 1

  return counter

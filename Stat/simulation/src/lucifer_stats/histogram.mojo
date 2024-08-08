from collections import List, Set

# return unique elements
fn unique(data: List[Int]) -> List[Int]:
  var unique = List[Int]()

  for ele in data:
    if ele[] not in unique:
      unique.append(ele[])

  return unique

fn histogram(data: List[Int]) -> (List[Int], List[Float64]): 
  var freqs = List[Float64]()
  var eles = unique(data)

  for ele in eles:
      var count = data.count(ele[])
      freqs.append((count/len(data)).cast[DType.float64]())

  return (eles, freqs)


  

from collections import List

from .utils import unique, contain, list_count

fn histogram[type: DType](data: List[Scalar[type]]) -> (List[Scalar[type]], List[Float64]): 
  var freqs = List[Float64]()
  var eles = unique(data)

  for ele in eles:
      var count = list_count(list=data, value=ele[])
      freqs.append(count.cast[DType.float64]()/len(data))

  return (eles, freqs)


from lucifer_stats.histogram import histogram

from lucifer_stats.utils import print_list

fn main():
  var data = List[Int64](1, 2, 2)
  
  var result = histogram(data)

  print_list(result[0])
  print_list(result[1])

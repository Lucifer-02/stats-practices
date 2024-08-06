from lucifer_stats.histogram import histogram

fn main():
  var data = List[Int](1,2,3)

  var x = histogram(data)

  for i in range(len(x[0])):
    print(x[0][i], ":", x[1][i])

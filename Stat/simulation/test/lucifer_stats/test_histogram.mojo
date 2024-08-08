from lucifer_stats.histogram import histogram

from testing import assert_equal

def test_histogram():
  var data = List[Int](1,2,3)
  result = histogram(data)
  expect = (List[Int](1,2,3), List[Float64](1/3,1/3,1/3))
  
  for i in range(len(data)): 
    assert_equal(result[0][i], expect[0][i])
    assert_equal(result[1][i], expect[1][i])

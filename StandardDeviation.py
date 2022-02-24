def standard_dev(data)
  # Length of array
  n = len(data)
  
  # Mean of array
  mean = sum(data)/n
  
  # std =  square root of variance
  stdev = sqrt(sum((x - mean) ** 2 for x in data) / (n-1))
  print(stdev)
  
  return stdev

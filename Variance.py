def variance(data):
  # Number of observations
  n = len(data)
  
  # Mean of the data
  mean = sum(data) / n
  
  # Square deviations
  deviations = [(x - mean) ** 2 for x in data]
  
  # Variance
  variance = sum(deviations) / n
  
  return variance


variance([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])

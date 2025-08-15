house_area = [1200, 1500, 1800, 2000, 2500]
house_price = [150000, 180000, 210000, 250000, 300000]

def model(x):
    # Calculate means
    mean_x = sum(house_area) / len(house_area)
    mean_y = sum(house_price) / len(house_price)
    
    # Calculate slope (m) and intercept (b)
    numerator = 0
    denominator = 0
    for i in range(len(house_area)):
        numerator += (house_area[i] - mean_x) * (house_price[i] - mean_y)
        denominator += (house_area[i] - mean_x) ** 2

    slope = numerator / denominator
    intercept = mean_y - slope * mean_x
    
    return slope * x + intercept

x = int(input("Enter the area of the house in square feet: "))
print("Predicted price:", model(x))

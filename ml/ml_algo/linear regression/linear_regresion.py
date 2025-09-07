house_area=[1200, 1500, 1800, 2000, 2500]
house_price=[150000, 180000, 210000, 250000, 300000]




def model(x):
    sum_x=0
    sum_y=0
    for i in range(len(house_area)):
        sum_x +=house_area[i]
        sum_y +=house_price[i]

    mean_x=sum_x/len(house_area)
    mean_y=sum_y/len(house_area)
    sum_x_x=0
    sum_y_y=0
    for i in range(len(house_area)):
        sum_x_x += abs(house_area[i]-mean_x)
        sum_y_y += abs(house_price[i]-mean_y)
    slope=((sum_x_x)*(sum_y_y))/(sum_x_x*sum_x_x)
    intercept=mean_y-slope*mean_x


    return slope*x+intercept



# reggressopn with multiple features

import numpy as np

x1=np.array([1200, 1500, 1800, 2000, 2500])
x2=np.array([3, 4, 2, 5, 4])# number of bedrooms
x3=np.array([3, 2, 4, 3, 5])# number of bathrooms
y1=np.array([150000, 180000, 210000, 250000, 300000])

def model1(x1, x2, x3):
    mean_x1 = np.mean(x1)
    mean_x2 = np.mean(x2)
    mean_x3 = np.mean(x3)
    mean_y1 = np.mean(y1)

    numerator1 = np.sum((x1 - mean_x1) * (y1 - mean_y1))
    denominator1 = np.sum((x1 - mean_x1) ** 2)

    numerator2 = np.sum((x2 - mean_x2) * (y1 - mean_y1))
    denominator2 = np.sum((x2 - mean_x2) ** 2)

    numerator3 = np.sum((x3 - mean_x3) * (y1 - mean_y1))
    denominator3 = np.sum((x3 - mean_x3) ** 2)

    slope1 = numerator1 / denominator1
    slope2 = numerator2 / denominator2
    slope3 = numerator3 / denominator3

    intercept = mean_y1 - (slope1 * mean_x1 + slope2 * mean_x2 + slope3 * mean_x3)

    return slope1 * x1 + slope2 * x2 + slope3 * x3 + intercept

xarea = int(input("Enter the area of the house in square feet: "))
xbedrooms = int(input("Enter the number of bedrooms: "))    
xbathrooms = int(input("Enter the number of bathrooms: "))
print("Predicted price:", model1(xarea, xbedrooms, xbathrooms))
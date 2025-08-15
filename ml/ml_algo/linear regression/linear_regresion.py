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

x=input("Enter the area of the house in square feet: ")
x = int(x)
print(model(x))
class cars:
    def __init__(specification,brand,no):
      specification.brand = brand
      specification.no = no
    def myfunc(specifiction):
        print("car brand is "+ specifiction.brand)
        print("car no is " + specifiction.no)
p1=cars("kia","344") 
p1.myfunc()


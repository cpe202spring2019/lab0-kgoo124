def weight_on_planets():
   weight = int(input("What do you weigh on earth? "))
   print('\nOn Mars you would weigh {:.2f} pounds.\nOn Jupiter you would weigh {:.2f} pounds.'.format(weight * 0.38, weight * 2.34))
   
   
   
if __name__ == '__main__':
   weight_on_planets()

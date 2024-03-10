##########################################################
#                                                        #
# Program Name: Critical Values for Significance Tests   #
# Written by: Cristian Cannella                          #
# Date: March 10th 2024                                  #
#                                                        #
##########################################################

import math

def calc_t_one_sample():
    input_str = input("Enter values for x-bar, mu, std. dev, n\nseparated by spaces:\n")
    input_lst = input_str.split()
    xbar, mu, stddev, n = list(map(float, input_lst))
    numerator = xbar-mu
    denom = stddev/math.sqrt(n)
    t = numerator/denom
    return t

def calc_t_two_sample():
    #for population 1
    input_str_pop1 = input("Enter values for x-bar1, std. dev1, n1\nseparated by spaces:\n")
    input_lst_pop1 = input_str_pop1.split()
    xbar1, stddev1, n1 = list(map(float, input_lst_pop1))

    #for population 2
    input_str_pop2 = input("Enter values for x-bar2, std. dev2, n2\nseparated by spaces:\n")
    input_lst_pop2 = input_str_pop2.split()
    xbar2, stddev2, n2 = list(map(float, input_lst_pop2))

    dif_mu1_mu2 = float(input("Enter mu1-mu2:\n"))

    standard_error = math.sqrt((stddev1**2/n1) + (stddev2**2/n2))
    numerator = (xbar1-xbar2) - (dif_mu1_mu2)

    t = numerator/standard_error
    return t

def calc_z_one_sample():
    input_str = input("Enter values for p-hat, p-naught, n\nseparated by spaces:\n")
    input_lst = input_str.split()
    p_hat, p_naught, n = list(map(float, input_lst))

    p_naught_comp = 1-p_naught
    numerator = p_hat-p_naught
    standard_error = math.sqrt((p_naught*p_naught_comp)/n)
    z = numerator/standard_error
    return z

def calc_z_two_sample():
    #for population 1
    input_str_pop1 = input("Enter values for p-hat1, n1\nseparated by spaces:\n")
    input_lst_pop1 = input_str_pop1.split()
    p_hat_1, n1 = list(map(float, input_lst_pop1))

    #for population 2
    input_str_pop2 = input("Enter values for p-hat2, n2\nseparated by spaces:\n")
    input_lst_pop2 = input_str_pop2.split()
    p_hat_2, n2 = list(map(float, input_lst_pop2))

    #Get the difference between population parameters (should usually be 0, but just in case!)
    dif_p1_p2 = float(input("Enter (p-naught1)-(p-naught2):\n"))

    #for pooled population
    x1 = p_hat_1*n1
    x2 = p_hat_2*n2
    p_hat_pooled = (x1+x2)/(n1+n2)
    p_hat_pooled_comp = 1-p_hat_pooled

    #Ok let's calculate z finally
    numerator = (p_hat_1-p_hat_2)-dif_p1_p2
    standard_error = math.sqrt((p_hat_pooled*p_hat_pooled_comp)*((1/n1) + (1/n2)))
    z = numerator/standard_error
    return z
    
#Main loop
running = True
while(running):

    print("Calculate Critical Values for Significance Tests\n1: t*\n2: z*\n3: Exit")
    z_or_t = int(input("Choose: ")) 

    if(z_or_t == 1):
        test_type = int(input("1: One Sample\n2: Two Sample\n3: Paired\n4: Exit\nChoose: "))
        if(test_type == 1 or test_type == 3):
            print(calc_t_one_sample())
        elif(test_type == 2):
            print(calc_t_two_sample())
        else:
            running = False

    elif(z_or_t == 2):
        test_type = int(input("1: One Sample\n2: Two Sample\n3: Exit\nChoose: "))
        if(test_type == 1):
            print(calc_z_one_sample())
        elif(test_type == 2):
            print(calc_z_two_sample())
        else:
            running = False

    else:
        running = False

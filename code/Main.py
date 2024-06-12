#Nguyen, Duc Viet

# import packages
import pandas as pd
import matplotlib.pyplot as plt
import functions as f
import seaborn as sns
import numpy as np
from sklearn.preprocessing import PolynomialFeatures


# show menu program
f.show_menu()

# user choose which option to execute
print('Wellcome!')
print('Please type 1 or 2\n')
# program check valid user input
choice = f.check_input()

# execute option corresponding to user's choice
# program will only be execute by non-0 input,
# type 0 to exit
while choice !=0:
    if choice == 1 or choice == 2:

        # option 1: analysing data from users
        if choice == 1:
            path = input('\nType your CSV file path\n')

        # Option 2: analysing built-in data
        else:
            path = 'code/data_tree.csv'

        # read data with error handing. Retype with wrong file path
        while True:
            try:
                data = pd.read_csv(path)
                break
            except:
                print("\nFile path is wrong! Please check and try again.")
                path = input('Type your CSV file path\n')

        ##Descriptive statistic
        # data preparation
        data = data.dropna() #remove raw containing null values to avoid errors
        dbh = data["DBH"] 
        h = data["H"] 
        bio = data["AGB"]
                
        # print the data
        print('\n',"-"*50)
        print('The data was imported, take a look:\n')
        print(data)

        input("Enter to continue!")

        # basic statistic of the data
        include =['object', 'float', 'int'] #list of data types to analyse
        print('\n',"-"*50)
        print('\nOverview of the data:\n')
        desc = data.describe(include=include)
        print(desc)

        input("Enter to continue!")

        # pairwise correlation of all columns
        print('\n',"-"*50)
        print('\nData correlation:\n')
        corr = sns.heatmap(data.corr(),annot=True,cmap='gray')
        plt.show()

        input("Enter to continue!")

        # visualize DBH, H and Biomass relationship
        print('\n',"-"*50)
        print('\nData relationship visualization\n')
        f.plot_relation(dbh, h, bio)
        
        input("Enter to continue!")
        
        ## Allometric equation for biomass
        # data preparation
        dbh_h = data[['DBH','H']]
        #reshape dbh,h variable to two-dimensional
        dbh_re = np.array(dbh).reshape((-1,1))
        h_re = np.array(h).reshape((-1,1))
        #DBH^2
        dbh2 = dbh**2
        dbh2_re = np.array(dbh2).reshape((-1,1))
        #ln(DBH)
        dbh_ln = np.log(dbh)
        dbh_ln_re = np.array(dbh_ln).reshape((-1,1))
        #log(DBH)
        dbh_log = np.log10(dbh)
        dbh_log_re = np.array(dbh_log).reshape((-1,1))
        #H^2
        h2 = h**2
        h2_re = np.array(h2).reshape((-1,1))
        #DBH^2 and H^2
        data['DBH2'] = dbh2
        data['H2'] = h2
        dbh2_h2 = data[['DBH2','H2']]
        #log(DBH^2*H)
        dbh2h_log = np.log10(dbh2*h)
        dbh2h_log_re = np.array(dbh2h_log).reshape((-1,1))
        #Transform DBH to DBH^2
        transformer = PolynomialFeatures(degree=2, include_bias=False)
        transformer.fit(dbh_re)
        dbh2_re2 = transformer.transform(dbh_re)
        
        # apply 10 allometric equation
        print('\n',"-"*50)
        print('\nAllometric equation')
        f.equation1(dbh_re, bio)
        input("Enter to continue!")
        f.equation2(h_re, bio)
        input("Enter to continue!")
        f.equation3(dbh, h, dbh_h, bio)
        input("Enter to continue!")
        f.equation4(dbh2_re, bio)
        input("Enter to continue!")
        f.equation5(dbh, dbh2, dbh2_re2, bio)
        input("Enter to continue!")
        f.equation6(dbh_ln, dbh_ln_re, bio)
        input("Enter to continue!")
        f.equation7(dbh_log, dbh_log_re, bio)
        input("Enter to continue!")
        f.equation8(dbh2, h2, dbh2_h2, bio)
        input("Enter to continue!")
        f.equation9(dbh2h_log_re, bio)
        input("Enter to continue!")
        f.equation10(dbh, h, bio)
        
        print('\n')
        print('*'*50)
        print('\nThe processing is finish. Thank you for using the program!')
        
    # retype for wrong input to select which option to execute
    else:
        print('\nWrong input! There is no such option')
        print('Please type again 1 or 2')

    # select which option for the next loop
    f.show_menu()
    choice = f.check_input()

# farewell when exiting the program
print('\nThank you for using the program')
print('See you again!')

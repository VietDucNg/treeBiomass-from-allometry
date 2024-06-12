#Nguyen, Duc Viet

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from scipy.optimize import minimize
from sklearn.metrics import r2_score

#function show menu program
def show_menu():
    print('\n')
    print('---------------------------')
    print('BIOMASS CALCULATION PROGRAM')
    print('---------------------------')
    print('1. User-defined data')
    print('2. Buil-in data')
    print('(Press 0 to exit)')
    print('---------------------------')
    print('\n')

#function ask for user input and check if user input is integer
def check_input():
    while True:
        try:
            choice = int(input())
            break
        except ValueError:
            print('\nWrong input! There is no such option')
            print('Please type again 1 or 2')
            show_menu()
    return choice

#function plot data relationship
def plot_relation(dbh,h,bio):  
    fig, ax = plt.subplots(nrows=2, ncols=3,figsize=(12,7))
    ax[0,0].hist(dbh, bins=30, align='mid', color='gray')
    ax[0,0].set_ylabel('Count')
    ax[0,0].set_xlabel('DBH (cm)')
    ax[0,0].set_title('(a)')
    
    ax[0,1].hist(h, bins=30, align='mid', color='gray')
    ax[0,1].set_ylabel('Count')
    ax[0,1].set_xlabel('Height (m)')
    ax[0,1].set_title('(b)')
    
    ax[0,2].hist(bio, bins=20, align='mid', color='gray')
    ax[0,2].set_ylabel('Count')
    ax[0,2].set_xlabel('Biomass (kg)')
    ax[0,2].set_title('(c)')
    
    ax[1,0].scatter(dbh,h,s=7,color='gray')
    ax[1,0].set_ylabel('Height (m)')
    ax[1,0].set_xlabel('DBH (cm)')
    ax[1,0].set_title('(d)')
    
    ax[1,1].scatter(dbh,bio,s=7,color='gray')
    ax[1,1].set_ylabel('Biomass (m)')
    ax[1,1].set_xlabel('DBH (cm)')
    ax[1,1].set_title('(e)')
    
    ax[1,2].scatter(h,bio,s=7,color='gray')
    ax[1,2].set_ylabel('Biomass (m)')
    ax[1,2].set_xlabel('Height (m)')
    ax[1,2].set_title('(f)')
    
    plt.tight_layout() #adjust layout that avoid overlap between subplots
    plt.suptitle('Figure1. DBH distribution (a), height distribution (b), \nBiomass distribution (c) and their relationship (d-f)', y=1.1)
    plt.show()
    plt.close()

#Equation 1 : Biomass = a + b*DBH
def equation1(dbh_re, bio):
    eq1 = LinearRegression().fit(dbh_re, bio)
    print('*'*50)
    print('\nEquation 1: Biomass = a + b*DBH')
    print('intercept (a):', eq1.intercept_)
    print('slope (b):', eq1.coef_)
    
    #visualization
    bio_pred1 = eq1.predict(dbh_re)
    
    fig, ax = plt.subplots()
    ax.scatter(dbh_re, bio,color='gray',alpha=0.7)
    ax.plot(dbh_re,bio_pred1,color = 'black')
    ax.set_xlabel('DBH (cm)')
    ax.set_ylabel('Biomass (kg)')
    ax.set_title('Equation 1')
    plt.tight_layout()
    plt.show()
    plt.close()
    
    #evaluating the Equation
    r2_eq1 = eq1.score(dbh_re, bio)
    mae_eq1 = metrics.mean_absolute_error(bio, bio_pred1)
    mse_eq1 = metrics.mean_squared_error(bio, bio_pred1)
    rmse_eq1 = np.sqrt(metrics.mean_squared_error(bio, bio_pred1))
    print('\nCoefficient of determination (R-squared): {:.2f}'.format(r2_eq1))
    print('Mean Absolute Error (MAE): {:.2f}'.format(mae_eq1))
    print('Mean Square Error (MSE): {:.2f}'.format(mse_eq1))
    print('Root Mean Square Error (RMSE): {:.2f}'.format(rmse_eq1))
    
#Equation 2 : Biomass = a + b*H
def equation2(h_re,bio):
    eq2 = LinearRegression().fit(h_re, bio)
    print('*'*50)
    print('\nEquation 2: Biomass = a + b*height')
    print('intercept (a):', eq2.intercept_)
    print('slope (b):', eq2.coef_)
    
    #visualization
    bio_pred2 = eq2.predict(h_re)
    
    fig, ax = plt.subplots()
    ax.scatter(h_re, bio,color='gray',alpha=0.7)
    ax.plot(h_re,bio_pred2,color = 'black')
    ax.set_xlabel('H (m)')
    ax.set_ylabel('Biomass (kg)')
    ax.set_title('Equation 2')
    plt.tight_layout()
    plt.show()
    plt.close()
    
    #evaluating the Equation
    r2_eq2 = eq2.score(h_re, bio)
    mae_eq2 = metrics.mean_absolute_error(bio, bio_pred2)
    mse_eq2 = metrics.mean_squared_error(bio, bio_pred2)
    rmse_eq2 = np.sqrt(metrics.mean_squared_error(bio, bio_pred2))
    print('\nCoefficient of determination (R-squared): {:.2f}'.format(r2_eq2))
    print('Mean Absolute Error (MAE): {:.2f}'.format(mae_eq2))
    print('Mean Square Error (MSE): {:.2f}'.format(mse_eq2))
    print('Root Mean Square Error (RMSE): {:.2f}'.format(rmse_eq2))

#equation 3 : Biomass = a + b*DBH + c*H
def equation3(dbh, h, dbh_h, bio):
    eq3 = LinearRegression().fit(dbh_h, bio)
    print('*'*50)
    print('\nEquation 3: Biomass = a + b*DBH + c*H')
    print('intercept (a):', eq3.intercept_)
    print('slope (b,c):', eq3.coef_)
    
    #visualization
    x_pred = np.linspace(0, 30, 30)   # range of DBH
    y_pred = np.linspace(0, 100, 30)  # range of H
    dbh_pred, h_pred = np.meshgrid(x_pred, y_pred)
    dbh_h_viz = np.array([dbh_pred.flatten(), h_pred.flatten()]).T
    
    bio_pred3 = eq3.predict(dbh_h)
    bio_pred_viz = eq3.predict(dbh_h_viz)
     
    fig = plt.figure(figsize=(12,4))
    
    ax1 = fig.add_subplot(131, projection='3d')
    ax2 = fig.add_subplot(132, projection='3d')
    ax3 = fig.add_subplot(133, projection='3d')
    
    axes = [ax1, ax2, ax3]
    
    for ax in axes:
        ax.plot(dbh,h,bio, zorder = 15,linestyle='none', color = 'gray',marker='o', alpha=0.5)
        ax.scatter(dbh_pred.flatten(),h_pred.flatten(),bio_pred_viz, facecolor=(0,0,0,0), s=20, edgecolor='#70b3f0')
        ax.set_xlabel('DBH (cm)')
        ax.set_ylabel('H (m)')
        ax.set_zlabel('Biomass (kg)')
    
    
    ax1.view_init(elev=28, azim=120)
    ax2.view_init(elev=4, azim=114)
    ax3.view_init(elev=60, azim=165)
    
    fig.suptitle('Equation 3')
    fig.tight_layout()
    plt.show()
    plt.close()
    
    #evaluating the Equation
    r2_eq3 = eq3.score(dbh_h, bio)
    mae_eq3 = metrics.mean_absolute_error(bio, bio_pred3)
    mse_eq3 = metrics.mean_squared_error(bio, bio_pred3)
    rmse_eq3 = np.sqrt(metrics.mean_squared_error(bio, bio_pred3))
    print('\nCoefficient of determination (R-squared): {:.2f}'.format(r2_eq3))
    print('Mean Absolute Error (MAE): {:.2f}'.format(mae_eq3))
    print('Mean Square Error (MSE): {:.2f}'.format(mse_eq3))
    print('Root Mean Square Error (RMSE): {:.2f}'.format(rmse_eq3))

#equation 4: Biomass = a + b*DBH^2
def equation4(dbh2_re,bio):
    eq4 = LinearRegression().fit(dbh2_re, bio)
    print('*'*50)
    print('\nEquation 4: Biomass = a + b*DBH^2')
    print('intercept (a):', eq4.intercept_)
    print('slope (b):', eq4.coef_)
    
    #visualization
    bio_pred4 = eq4.predict(dbh2_re)
    
    fig, ax = plt.subplots()
    ax.scatter(dbh2_re, bio,color='gray',alpha=0.7)
    ax.plot(dbh2_re,bio_pred4,color = 'black')
    ax.set_xlabel('DBH^2 (cm)')
    ax.set_ylabel('Biomass (kg)')
    ax.set_title('Equation 4')
    plt.tight_layout()
    plt.show()
    plt.close()
    
    #evaluating the Equation
    r2_eq4 = eq4.score(dbh2_re, bio)
    mae_eq4 = metrics.mean_absolute_error(bio, bio_pred4)
    mse_eq4 = metrics.mean_squared_error(bio, bio_pred4)
    rmse_eq4 = np.sqrt(metrics.mean_squared_error(bio, bio_pred4))
    print('\nCoefficient of determination (R-squared): {:.2f}'.format(r2_eq4))
    print('Mean Absolute Error (MAE): {:.2f}'.format(mae_eq4))
    print('Mean Square Error (MSE): {:.2f}'.format(mse_eq4))
    print('Root Mean Square Error (RMSE): {:.2f}'.format(rmse_eq4))
    
#equation 5: Biomass = a + b*DBH + c*DBH^2
def equation5(dbh, dbh2, dbh2_re2, bio):
    eq5 = LinearRegression().fit(dbh2_re2, bio)
    print('*'*50)
    print('\nequation 5: Biomass = a + b*DBH + c*DBH^2')
    print('intercept (a):', eq5.intercept_)
    print('slope (b,c):', eq5.coef_)
    
    #visualization
    x_pred = np.linspace(0, 30, 30)   # range of DBH
    y_pred = np.linspace(0, 1000, 30)  # range of H
    dbh_pred, dbh2_pred = np.meshgrid(x_pred, y_pred)
    xy_viz = np.array([dbh_pred.flatten(), dbh2_pred.flatten()]).T
    
    bio_pred5 = eq5.predict(dbh2_re2)
    bio_pred_viz = eq5.predict(xy_viz)
     
    fig = plt.figure(figsize=(12,4))
    
    ax1 = fig.add_subplot(131, projection='3d')
    ax2 = fig.add_subplot(132, projection='3d')
    ax3 = fig.add_subplot(133, projection='3d')
    
    axes = [ax1, ax2, ax3]
    
    for ax in axes:
        ax.plot(dbh,dbh2,bio, zorder = 15,linestyle='none', color = 'gray',marker='o', alpha=0.5)
        ax.scatter(dbh_pred.flatten(),dbh2_pred.flatten(),bio_pred_viz, facecolor=(0,0,0,0), s=20, edgecolor='#70b3f0')
        ax.set_xlabel('DBH (cm)')
        ax.set_ylabel('DBH^2 (cm)')
        ax.set_zlabel('Biomass (kg)')
    
    
    ax1.view_init(elev=28, azim=120)
    ax2.view_init(elev=4, azim=114)
    ax3.view_init(elev=60, azim=165)
    
    fig.suptitle('Equation 5')
    fig.tight_layout()
    plt.show()
    plt.close()
    
    #evaluating the Equation
    r2_eq5 = eq5.score(dbh2_re2, bio)
    mae_eq5 = metrics.mean_absolute_error(bio, bio_pred5)
    mse_eq5 = metrics.mean_squared_error(bio, bio_pred5)
    rmse_eq5 = np.sqrt(metrics.mean_squared_error(bio, bio_pred5))
    print('\nCoefficient of determination (R-squared): {:.2f}'.format(r2_eq5))
    print('Mean Absolute Error (MAE): {:.2f}'.format(mae_eq5))
    print('Mean Square Error (MSE): {:.2f}'.format(mse_eq5))
    print('Root Mean Square Error (RMSE): {:.2f}'.format(rmse_eq5))
    
# Equation 6: Biomass = a + b*ln(DBH)
def equation6(dbh_ln, dbh_ln_re, bio):
    eq6 = LinearRegression().fit(dbh_ln_re, bio)
    print('*'*50)
    print('\nEquation 6: Biomass = a + b*ln(DBH)')
    print('intercept (a):', eq6.intercept_)
    print('slope (b):', eq6.coef_)
    
    #visualization
    bio_pred6 = eq6.predict(dbh_ln_re)
    
    fig, ax = plt.subplots()
    ax.scatter(dbh_ln_re, bio,color='gray',alpha=0.7)
    ax.plot(dbh_ln_re,bio_pred6,color = 'black')
    ax.set_xlabel('ln(DBH) (cm)')
    ax.set_ylabel('Biomass (kg)')
    ax.set_title('Equation 6')
    plt.tight_layout()
    plt.show()
    plt.close()
    
    #evaluating the Equation
    r2_eq6 = eq6.score(dbh_ln_re, bio)
    mae_eq6 = metrics.mean_absolute_error(bio, bio_pred6)
    mse_eq6 = metrics.mean_squared_error(bio, bio_pred6)
    rmse_eq6 = np.sqrt(metrics.mean_squared_error(bio, bio_pred6))
    print('\nCoefficient of determination (R-squared): {:.2f}'.format(r2_eq6))
    print('Mean Absolute Error (MAE): {:.2f}'.format(mae_eq6))
    print('Mean Square Error (MSE): {:.2f}'.format(mse_eq6))
    print('Root Mean Square Error (RMSE): {:.2f}'.format(rmse_eq6))
    
# Equation 7: Biomass = a + b*log(DBH)
def equation7(dbh_log, dbh_log_re, bio):
    eq7 = LinearRegression().fit(dbh_log_re, bio)
    print('*'*50)
    print('\nEquation 7: Biomass = a + b*log(DBH)')
    print('intercept (a):', eq7.intercept_)
    print('slope (b):', eq7.coef_)

    #visualization
    bio_pred7 = eq7.predict(dbh_log_re)

    fig, ax = plt.subplots()
    ax.scatter(dbh_log_re, bio,color='gray',alpha=0.7)
    ax.plot(dbh_log_re,bio_pred7,color = 'black')
    ax.set_xlabel('log(DBH) (cm)')
    ax.set_ylabel('Biomass (kg)')
    ax.set_title('Equation 7')
    plt.tight_layout()
    plt.show()
    plt.close()

    #evaluating the Equation
    r2_eq7 = eq7.score(dbh_log_re, bio)
    mae_eq7 = metrics.mean_absolute_error(bio, bio_pred7)
    mse_eq7 = metrics.mean_squared_error(bio, bio_pred7)
    rmse_eq7 = np.sqrt(metrics.mean_squared_error(bio, bio_pred7))
    print('\nCoefficient of determination (R-squared): {:.2f}'.format(r2_eq7))
    print('Mean Absolute Error (MAE): {:.2f}'.format(mae_eq7))
    print('Mean Square Error (MSE): {:.2f}'.format(mse_eq7))
    print('Root Mean Square Error (RMSE): {:.2f}'.format(rmse_eq7))

#equation 8 : Biomass = a + b*DBH^2 + c*H^2
def equation8(dbh2, h2, dbh2_h2, bio):
    eq8 = LinearRegression().fit(dbh2_h2, bio)
    print('*'*50)
    print('\nEquation 8 : Biomass = a + b*DBH^2 + c*H^2')
    print('intercept (a):', eq8.intercept_)
    print('slope (b,c):', eq8.coef_)
    
    #visualization
    x_pred = np.linspace(0, 1000, 30)
    y_pred = np.linspace(0, 1000, 30)
    dbh_pred, h_pred = np.meshgrid(x_pred, y_pred)
    dbh_h_viz = np.array([dbh_pred.flatten(), h_pred.flatten()]).T
    
    bio_pred8 = eq8.predict(dbh2_h2)
    bio_pred_viz = eq8.predict(dbh_h_viz)
     
    fig = plt.figure(figsize=(12,4))
    
    ax1 = fig.add_subplot(131, projection='3d')
    ax2 = fig.add_subplot(132, projection='3d')
    ax3 = fig.add_subplot(133, projection='3d')
    
    axes = [ax1, ax2, ax3]
    
    for ax in axes:
        ax.plot(dbh2,h2,bio, zorder = 15,linestyle='none', color = 'gray',marker='o', alpha=0.5)
        ax.scatter(dbh_pred.flatten(),h_pred.flatten(),bio_pred_viz, facecolor=(0,0,0,0), s=20, edgecolor='#70b3f0')
        ax.set_xlabel('DBH^2 (cm)')
        ax.set_ylabel('H^2 (m)')
        ax.set_zlabel('Biomass (kg)')
    
    ax1.view_init(elev=28, azim=120)
    ax2.view_init(elev=4, azim=114)
    ax3.view_init(elev=60, azim=165)
    
    fig.suptitle('Equation 8')
    fig.tight_layout()
    plt.show()
    plt.close()
    
    #evaluating the Equation
    r2_eq8 = eq8.score(dbh2_h2, bio)
    mae_eq8 = metrics.mean_absolute_error(bio, bio_pred8)
    mse_eq8 = metrics.mean_squared_error(bio, bio_pred8)
    rmse_eq8 = np.sqrt(metrics.mean_squared_error(bio, bio_pred8))
    print('\nCoefficient of determination (R-squared): {:.2f}'.format(r2_eq8))
    print('Mean Absolute Error (MAE): {:.2f}'.format(mae_eq8))
    print('Mean Square Error (MSE): {:.2f}'.format(mse_eq8))
    print('Root Mean Square Error (RMSE): {:.2f}'.format(rmse_eq8))
    
#Equation 9 : Biomass = a + b*log(DBH^2*H)
def equation9(dbh2h_log_re, bio):
    eq9 = LinearRegression().fit(dbh2h_log_re, bio)
    print('*'*50)
    print('\nEquation 9: a + b*log(DBH^2*H)')
    print('intercept (a):', eq9.intercept_)
    print('slope (b):', eq9.coef_)
    
    #visualization
    bio_pred9 = eq9.predict(dbh2h_log_re)
    
    fig, ax = plt.subplots()
    ax.scatter(dbh2h_log_re, bio,color='gray',alpha=0.7)
    ax.plot(dbh2h_log_re,bio_pred9,color = 'black')
    ax.set_xlabel('log(DBH^2*H)')
    ax.set_ylabel('Biomass (kg)')
    ax.set_title('Equation 9')
    plt.tight_layout()
    plt.show()
    plt.close()
    
    #evaluating the Equation
    r2_eq9 = eq9.score(dbh2h_log_re, bio)
    mae_eq9 = metrics.mean_absolute_error(bio, bio_pred9)
    mse_eq9 = metrics.mean_squared_error(bio, bio_pred9)
    rmse_eq9 = np.sqrt(metrics.mean_squared_error(bio, bio_pred9))
    print('\nCoefficient of determination (R-squared): {:.2f}'.format(r2_eq9))
    print('Mean Absolute Error (MAE): {:.2f}'.format(mae_eq9))
    print('Mean Square Error (MSE): {:.2f}'.format(mse_eq9))
    print('Root Mean Square Error (RMSE): {:.2f}'.format(rmse_eq9))

#Equation 10 : Biomass = a*DBH^b*H^c
def equation10(dbh, h, bio):
    #formular
    def calc_bio(x):
        a,b,c = x
        y = a*(dbh**b)*(h**c)
        return y
    #define objective (SSE)
    def objective(x):
        return np.sum(((calc_bio(x)-bio)/bio)**2)
    # initial guesses
    x0 = np.zeros(3)
    #optimize SSE
    # bounds on variables
    bnds100 = (-100.0, 100.0)
    no_bnds = (-1.0e10, 1.0e10)
    bnds = (no_bnds, no_bnds, bnds100)
    solution = minimize(objective,x0,method='SLSQP',bounds=bnds)
    x = solution.x
    bio_pred10 = calc_bio(x)
    
    print('*'*50)
    print('\nEquation 10: Biomass = a*(DBH^b)*(H^c)')
    print('Parameter (a):{:.3f}'.format(x[0]))
    print('Parameter (b):{:.3f}'.format(x[1]))
    print('Parameter (c):{:.3f}'.format(x[2]))
    
    #visualization
    fig, ax = plt.subplots()
    ax.scatter(bio, bio_pred10,color='gray',alpha=0.7)
    a,b=np.polyfit(bio, bio_pred10, 1)
    ax.plot(bio, a*bio+b, color='black')
    ax.set_xlabel('Measured biomass (kg)')
    ax.set_ylabel('Predicted biomass (kg)')
    r2_eq10 = r2_score(bio, bio_pred10)
    ax.set_title('Equation 10')
    plt.tight_layout()
    plt.show()
    plt.close()
    
    #evaluating the Equation
    
    mae_eq10 = metrics.mean_absolute_error(bio, bio_pred10)
    mse_eq10 = metrics.mean_squared_error(bio, bio_pred10)
    rmse_eq10 = np.sqrt(metrics.mean_squared_error(bio, bio_pred10))
    print('\nCoefficient of determination (R-squared): {:.2f}'.format(r2_eq10))
    print('Mean Absolute Error (MAE): {:.2f}'.format(mae_eq10))
    print('Mean Square Error (MSE): {:.2f}'.format(mse_eq10))
    print('Root Mean Square Error (RMSE): {:.2f}'.format(rmse_eq10))

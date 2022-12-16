import matplotlib.pyplot as plt
import csv
import pandas as pd
import calendar

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)
try:
    df = pd.read_csv('comptagevelo2014.csv', parse_dates=['Date'], dayfirst=True)
    print('----------------TOTAL NUMBER OF CYCLERS FOR EVERY MONTH----------------\n')
    month_df = df.groupby(df['Date'].dt.strftime('%B'))[['Rachel / Papineau','Berri1', 'Maisonneuve_1', 'Maisonneuve_2', 'Brebeuf','Parc','PierDup','CSC (Cte Sainte-Catherine)','Pont_Jacques_Cartier','Totem_Laurier','Notre-Dame','Rachel / Hotel de Ville','Saint-Antoine','Ren-Lvesque','Viger','Boyer','Maisonneuve_3','University','Saint-Urbain']].sum()
    print(month_df)
    print('THE MOST POPULAR MONTH FOR CYCLERS IN 2014 IS', month_df.sum(axis=1).idxmax())
    months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
    RP_df = df.groupby(df['Date'].dt.strftime('%B'))['Rachel / Papineau'].sum().sort_index(key = lambda x : pd.Categorical(x, categories=months, ordered=True))
    RP_df.to_csv('Rachel_Papineau.csv',index=False)
    print('----------------INFORMATION ABOUT Rachel/Papineau TRACK, THAT WAS SAVED IN FILE----------------\n')
    print(RP_df)
    RP_df.plot.bar(figsize=(15, 10))
    spring_df = df[59:151] 
    #print(spring_df)
    day_df = spring_df.groupby(df['Date'].dt.strftime('%A'))[['Berri1', 'Maisonneuve_1', 'Maisonneuve_2', 'Brebeuf']].sum()
    print('The least popular day in spring is', day_df.sum(axis=1).idxmin())
    plt.xlabel('Month') 
    plt.ylabel('Cyclers')
    plt.title('Amount of cyclers on Rachel/Papineau')
    plt.show()
except:
    print('file not found')
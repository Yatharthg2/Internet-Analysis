import pandas as pd
import matplotlib.pyplot as plt

def Show_all_record():
    df = pd.read_csv(file_name, usecols=["Countries", "Code", "Year", "Mobile cellular subscriptions (per 100 people)", "Individuals using the Internet (% of population)"])
    print(df.to_string())
    return

def Show_Country():
    df = pd.read_csv(file_name)
    print(df["Countries"].unique())
    return

def Add_Record():
    df = pd.read_csv(file_name, usecols=["Countries", "Code", "Year", "Mobile cellular subscriptions (per 100 people)", "Individuals using the Internet (% of population)"])
    col = df.columns
    df = df.head(0)
    j = 0
    p_insert = {}
    for i in col:
        print("Enter ", col[j])
        p_input = input()
        p_insert[col[j]] = p_input
        j = j + 1
    df = df.append(p_insert, ignore_index=True)
    df.to_csv(file_name, mode='a', header=False)
    print("Record Added Successfully")
    return

def Delete_Record():
    while True:
        df = pd.read_csv(file_name,
                         usecols=["Countries", "Code", "Year", "Mobile cellular subscriptions (per 100 people)", "Individuals using the Internet (% of population)"])
        p_deleted = input(" Enter the Country Name to be Deleted :  ")
        if df.index[df['Countries'] == p_deleted] > 0:
            df.drop(df.index[df['Countries'] == p_deleted], inplace=True)
            df.to_csv(file_name)
            print("Country Record Deleted Successfully ")
            break
        else:
            print("Country Record Does Not Exists ")
            print("\n")
            retry = input("Do you want to Retry (Y/N) ? ")
            if retry == 'Y' or retry == 'y':
                continue
            else:
                break
    return

def Update_Record():
    while True:
        df = pd.read_csv(file_name,
                         usecols=["Countries", "Code", "Year", "Mobile cellular subscriptions (per 100 people)", "Individuals using the Internet (% of population)"])
        p_mod = input(" Enter the Country Name For Details to be Updated :  ")
        if df.index[df['Countries'] == p_mod] > 0:
            print("What needs to be Updated ? ")
            print("Enter 1 For Country Name ")
            print("Enter 2 For Code ")
            print("Enter 3 For Year")
            print("Enter 4 For Subscription ")
            print("Enter 5 For % of population ")
            mod_choice = int(input(" Enter Your Choice(1..5) "))
            if mod_choice == 1:
                new_name = input("Enter Country New Name : ")
                df.loc[(df['Countries'] == p_mod), ['Countries']] = new_name
                df.to_csv(file_name)
                print("Country Name Updated Successfully ")
                print("\n")
                print("1. Update Details of Other Country")
                print("2. Back to Main Menu")
                sub_choice = int(input(" Enter your Choice (1..2) : "))
                if sub_choice == 1:
                    continue
                else:
                    break
            elif mod_choice == 2:
                new_Code = input("Enter New Code For Country : ")
                df.loc[(df['Countries'] == p_mod), ['Code']] = new_Code
                df.to_csv(file_name)
                print("Country Code Updated Successfully ")
                print("\n")
                print("1. Update Details of Other Country")
                print("2. Back to Main Menu")
                sub_choice = int(input(" Enter your Choice (1..2) : "))
                if sub_choice == 1:
                    continue
                else:
                    break
            elif mod_choice == 3:
                new_Year = input("Enter New Year For Country : ")
                df.loc[(df['Countries'] == p_mod), ['Year']] = new_Year
                df.to_csv(file_name)
                print("Country Year Updated Successfully ")
                print("\n")
                print("1. Update Details of Other Player")
                print("2. Back to Main Menu")
                sub_choice = int(input(" Enter your Choice (1..2) : "))
                if sub_choice == 1:
                    continue
                else:
                    break
            elif mod_choice == 4:
                new_sub = input("Enter New Subscription : ")
                df.loc[(df['Countries'] == p_mod), ['Mobile cellular subscriptions (per 100 people)']] = new_sub
                df.to_csv(file_name)
                print("Country Subscription data Updated Successfully ")
                print("\n")
                print("1. Update Details of Other Country")
                print("2. Back to Main Menu")
                sub_choice = int(input(" Enter your Choice (1..2) : "))
                if sub_choice == 1:
                    continue
                else:
                    break
            elif mod_choice == 5:
                new_sub = input("Enter New % of population : ")
                df.loc[(df['Countries'] == p_mod), ['Individuals using the Internet (% of population)']] = new_sub
                df.to_csv(file_name)
                print("% of population data Updated Successfully \n")
                print("1 For Update Details of Other Country")
                print("2 For Back to Main Menu")
                sub_choice = int(input(" Enter your Choice (1..2) : "))
                if sub_choice == 1:
                    continue
                else:
                    break
            else:
                continue
        else:
            print("Country Does Not Exists ")
            print("\n")
            retry = input("Do you want to Retry (Y/N) ? ")
            if retry == 'Y' or retry == 'y':
                continue
            else:
                break
    return

def Search_Record():
    while True:
        df = pd.read_csv(file_name,
                         usecols=["Countries", "Code", "Year", "Mobile cellular subscriptions (per 100 people)", "Individuals using the Internet (% of population)"])
        p_search = input(" Enter the Country Name to be Searched :  ")
        if df.index[df['Countries'] == p_search].all() > 0:
            print(df[df['Countries'] == p_search].to_string(), "\n")
            print("1 For Search More Countries")
            print("2 For Back to Main Menu")
            sub_choice = int(input(" Enter your Choice (1..2) : "))
            if sub_choice == 1:
                continue
            else:
                break
        else:
            print("Country Does Not Exists ")
            print("\n")
            retry = input("Do you want to Retry (Y/N) ? ")
            if retry == 'Y' or retry == 'y':
                continue
            else:
                break
    return

def Stats():
    while True:
        print("Enter 1 To View Top 10 Countries with Most Subscription ")
        print("Enter 2 To View Top 10 Countries with Least Subscription ")
        print("Enter 3 To View Top 10 Countries with Most % of population ")
        print("Enter 4 To View Top 10 Countries with Least % of population ")
        print("5 For Back to Main Menu")
        sub_choice = int(input("Enter your choice (1..5) : "))
        df = pd.read_csv(file_name,
                         usecols=["Countries", "Code", "Year", "Mobile cellular subscriptions (per 100 people)",
                                  "Individuals using the Internet (% of population)"])
        if sub_choice == 1:
            df = df.sort_values(['Mobile cellular subscriptions (per 100 people)'], ascending=False)
            df = df.head(10)
            print(df.to_string(), "\n")
            print("1 For More Stats")
            print("2 For Back to Main Menu")
            sub_choice = int(input(" Enter your Choice (1..2) : "))
            if sub_choice == 1:
                continue
            else:
                break
        elif sub_choice == 2:
            df = df.sort_values(['Mobile cellular subscriptions (per 100 people)'], ascending=True)
            df = df.head(10)
            print(df.to_string(), "\n")
            print("1 For More Stats")
            print("2 For Back to Main Menu")
            sub_choice = int(input(" Enter your Choice (1..2) : "))
            if sub_choice == 1:
                continue
            else:
                break
        elif sub_choice == 3:
            df = df.sort_values(['Individuals using the Internet (% of population)'], ascending=False)
            df = df.head(10)
            print(df.to_string(), "\n")
            print("1 For More Stats")
            print("2 For Back to Main Menu")
            sub_choice = int(input(" Enter your Choice (1..2) : "))
            if sub_choice == 1:
                continue
            else:
                break
        elif sub_choice == 4:
            df = df.sort_values(['Individuals using the Internet (% of population)'], ascending=True)
            df = df.head(10)
            print(df.to_string(), "\n")
            print("1 For More Stats")
            print("2 For Back to Main Menu")
            sub_choice = int(input(" Enter your Choice (1..2) : "))
            if sub_choice == 1:
                continue
            else:
                break
        else:
            print("Invalid Selection \n")
            retry = input("Do you want to Retry (Y/N) ? ")
            if retry == 'Y' or retry == 'y':
                continue
            else:
                break
    return

def Visualise_Record():
    while True:
        print("What Visualisation you Need  ? ")
        print("Enter 1 To View Top 5 Countries in terms of Most % of population")
        print("Enter 2 To View Top 5 Countries in terms of Least % of population")
        print("Enter 3 To View Top 5 Countries in terms of Most Subscription")
        print("Enter 4 To View Top 5 Countries in terms of Least Subscription")
        print("Enter 5 To View Top 5 Countries in terms of Most % of population & Most Subscription")
        print("Enter 6 To View Top 5 Countries in terms of Least % of population & Least Subscription")
        print("7 For Back to Main Menu")
        vis_choice = int(input(" Enter Your Choice(1..8) "))
        df = pd.read_csv(file_name,
                         usecols=["Countries", "Code", "Year", "Mobile cellular subscriptions (per 100 people)",
                                  "Individuals using the Internet (% of population)"])
        if vis_choice == 1:
            df = pd.read_csv(file_name)
            df = df.sort_values(['Individuals using the Internet (% of population)'], ascending=False)
            df = df.head(5)
            x = df['Countries']
            y = df['Individuals using the Internet (% of population)']
            df1 = pd.DataFrame(x, y)
            # plot
            plt.plot(x, y, label='Top 5 Countries')
            plt.xlabel('Country Name')
            plt.ylabel('% of population')
            plt.legend()
            plt.show()
            print("\n")
            print("1. Do you want to see more visualisation ? ")
            print("2. Back to Main Menu ")
            sub_choice = int(input(" Enter your Choice (1..2) : "))
            if sub_choice == 1:
                continue
            else:
                break
        elif vis_choice == 2:
            df = pd.read_csv(file_name)
            df = df.sort_values(['Individuals using the Internet (% of population)'], ascending=True)
            df = df.head(5)
            x = df['Countries']
            y = df['Individuals using the Internet (% of population)']
            # plot
            plt.xlabel('Country Name')
            plt.ylabel('% of population')
            plt.bar(x, y, color='m')
            plt.show()
            print("\n")
            print("1. Do you want to see more visualisation ? ")
            print("2. Back to Main Menu ")
            sub_choice = int(input(" Enter your Choice (1..2) : "))
            if sub_choice == 1:
                continue
            else:
                break
        elif vis_choice == 3:
            df = pd.read_csv(file_name)
            df = df.sort_values(['Mobile cellular subscriptions (per 100 people)'], ascending=False)
            df = df.head(5)
            x = df['Countries']
            y = df['Mobile cellular subscriptions (per 100 people)']
            plt.xlabel('Country Name')
            plt.ylabel('Subscription')
            plt.bar(x, y, color='m')
            plt.show()
            print("\n")
            print("1. Do you want to see more visualisation ? ")
            print("2. Back to Main Menu ")
            sub_choice = int(input(" Enter your Choice (1..2) : "))
            if sub_choice == 1:
                continue
            else:
                break
        elif vis_choice == 4:
            df = pd.read_csv(file_name)
            df = df.sort_values(['Mobile cellular subscriptions (per 100 people)'], ascending=True)
            df = df.head(5)
            x = df['Countries']
            y = df['Mobile cellular subscriptions (per 100 people)']
            # plot
            plt.plot(x, y, label='Top 5 Countries')
            plt.xlabel('Country Name')
            plt.ylabel('Subscription')
            plt.legend()
            plt.show()
            print("\n")
            print("1. Do you want to see more visualisation ? ")
            print("2. Back to Main Menu ")
            sub_choice = int(input(" Enter your Choice (1..2) : "))
            if sub_choice == 1:
                continue
            else:
                break
        elif vis_choice == 5:
            df = pd.read_csv(file_name)
            df = df[df['Individuals using the Internet (% of population)'] > 20]
            df = df.sort_values(
                ['Mobile cellular subscriptions (per 100 people)', 'Individuals using the Internet (% of population)'],
                ascending=False)
            df = df.head(5)
            x = df['Countries']
            y = df['Mobile cellular subscriptions (per 100 people)']
            # plot
            plt.plot(x, y, label='Subscription')
            x = df['Countries']
            y = df['Individuals using the Internet (% of population)']
            plt.plot(x, y, label='% of population')
            plt.xlabel('Countries')
            plt.ylabel('Performance')
            plt.legend()
            plt.show()
            print("\n")
            print("1 For Do you want to see more visualisation ? ")
            print("2 For Back to Main Menu ")
            sub_choice = int(input(" Enter your Choice (1..2) : "))
            if sub_choice == 1:
                continue
            else:
                break
        elif vis_choice == 6:
            df = pd.read_csv(file_name)
            df = df[df['Individuals using the Internet (% of population)'] > 20]
            df = df.sort_values(
                ['Mobile cellular subscriptions (per 100 people)', 'Individuals using the Internet (% of population)'],
                ascending=True)
            df = df.head(5)
            x = df['Countries']
            y = df['Mobile cellular subscriptions (per 100 people)']
            # plot
            plt.plot(x, y, label='Subscription')
            x = df['Countries']
            y = df['Individuals using the Internet (% of population)']
            plt.plot(x, y, label='% of population')
            plt.xlabel('Countries')
            plt.ylabel('Performance')
            plt.legend()
            plt.show()
            print("\n")
            print("1 For Do you want to see more visualisation ? ")
            print("2 For Back to Main Menu ")
            sub_choice = int(input(" Enter your Choice (1..2) : "))
            if sub_choice == 1:
                continue
            else:
                break
        elif vis_choice == 7:
            break
        else:
            print("Invalid Selection ")
            print("\n")
            retry = input("Do you want to Retry (Y/N) ? ")
            if retry == 'Y' or retry == 'y':
                continue
            else:
                break
    return

print("**** ---- ---- ---- ---- ---- ****")
print("      Internet Usage Analysis     ")
print("**** ---- ---- ---- ---- ---- ****\n")
file_name='Updated.csv'
while True:
    print("**** ---- -- Main Menu -- ---- ****")
    print("Press 1 For List of all Records ")
    print("Press 2 For List of all Countries ")
    print("Press 3 For Add a new Record ")
    print("Press 4 For Delete a Record ")
    print("Press 5 For Update a Record ")
    print("Press 6 For Visualization ")
    print("Press 7 For Search a Record ")
    print("Press 8 For Top Stats of Countries ")
    print("Press 9 For Exit")

    userchoice = int(input(" Enter your Choice (1..9) : "))
    if userchoice == 1:
        Show_all_record()
    elif userchoice == 2:
        Show_Country()
    elif userchoice == 3:
        Add_Record()
    elif userchoice == 4:
        Delete_Record()
    elif userchoice == 5:
        Update_Record()
    elif userchoice == 6:
        Visualise_Record()
    elif userchoice == 7:
        Search_Record()
    elif userchoice == 8:
        Stats()
    elif userchoice == 9:
        break


import login
#import n
#import indian_cuisine,chinese_cuisine,italin_cuisine,thai_cuisine
print("            Welcome to Cook or Buy 👨‍🍳🫕👩‍🍳 ",login.name,'😋')
buy = input("Do you want to buy food? (yes/no): ").lower()
if buy=='yes':
    import order
    order.buy()
else:
    while True:
        print("\n\nTypes of cuisines 🍽😋\n 1.Indian\n 2.Chinese\n 3.Italin\n "\
              "4.Thai\n 5.Mexican\n 6.Japanese")
        ch=int(input("\nWhich type of cuisne do you want?:"))
        import indian_cuisine,chinese_cuisine,italin_cuisine,thai_cuisines,mexcian_cuisine,japanese_cuisine
        if ch==1:
            indian_cuisine.indian()
        elif ch==2:
            chinese_cuisine.chinese()
        elif ch==3:
            italin_cuisine.italin()
        elif ch==4:
            thai_cuisines.thai()
        elif ch==5:
            mexcian_cuisine.mexican()
        elif ch==6:
            japanese_cuisine.japanese()
        else:
            print('\nPlease enter the correct number of that cuisine you want')
            continue
    
        con=int(input("\nDo you want to exit press 0: "))
        if con==0:
            break
        

   
        


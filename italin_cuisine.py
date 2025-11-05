from fpdf import FPDF
import pyttsx3
def italin():
    print('''\n\n🍝 Pasta Dishes:
1.Spaghetti Agli e Olio
2.Macaroni with Cheese
-------
🍕 Pizza:
3.Margherita pizza
4.Cheese Brust Pizza
-------
🧁 Desserts
5.Panna Cotta
6.Tiramisu
-------''')
    ch=int(input("Choose the dish number you want to try:"))
    if ch==1:
        Spaghetti="""Spaghetti Aglio e Olio Recipe
Prep Time: 5 minutes
Cook Time: 10 minutes
Total Time: 15 minutes
Serves: 2 people
Ingredients:
150g spaghetti
3 tbsp olive oil
4 to 5 garlic cloves, thinly sliced
1/2 tsp chili flakes
Salt to taste
Chopped parsley (optional)
Instructions:
1. Boil spaghetti with salt until al dente. Drain and reserve some water.
2. Heat olive oil, sauté garlic until golden.
3. Add chili flakes and cooked spaghetti. Toss well.
4. Add reserved water if needed. Garnish with parsley.
5. Serve hot with grated cheese if desired.
"""

        Spaghetti_ingre='''Ingredients:
150g spaghetti
3 tbsp olive oil
4 to 5 garlic cloves, thinly sliced
1/2 tsp chili flakes
Salt to taste
Chopped parsley (optional)'''
        # Split into words
        lines= Spaghetti.splitlines()

        # Text-to-speech setup
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)


        # Speak and show each word
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\Spaghetti.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10,Spaghetti_ingre)
            pdf.output("Spaghetti_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==2:
        Macaroni="""Macaroni and Cheese Recipe
Prep Time: 10 minutes
Cook Time: 15 minutes
Total Time: 25 minutes
Serves: 2 to 3 people
Ingredients:
1 cup macaroni
1 tbsp butter
1 tbsp all-purpose flour
1 cup milk
1/2 cup grated cheese (cheddar or processed)
Salt and pepper to taste
Instructions:
1. Boil macaroni in salted water until cooked. Drain and keep aside.
2. In another pan, melt butter and add flour. Stir for 1 minute.
3. Slowly add milk, stirring to avoid lumps.
4. Cook until it thickens. Add cheese, salt, and pepper.
5. Add cooked macaroni and mix well. Serve hot.
"""
        Macaroni_ingre='''Ingredients:
1 cup macaroni
1 tbsp butter
1 tbsp all-purpose flour
1 cup milk
1/2 cup grated cheese (cheddar or processed)
Salt and pepper to taste'''
        lines= Macaroni.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\macroni.jpeg")
        img.show()         
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, Macaroni_ingre)
            pdf.output("Macaroni_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==3:
        Margherita="""Margherita Pizza Recipe
Prep Time: 15 minutes
Cook Time: 15 minutes
Total Time: 30 minutes
Serves: 2 to 3 people
Ingredients:
1 pizza base (store-bought or homemade)
1/2 cup pizza sauce
1 cup grated mozzarella cheese
Fresh basil leaves
1/2 tsp oregano, 1/2 tsp chili flakes
1 tbsp olive oil
Instructions:
1. Preheat oven to 220°C (428°F).
2. Spread pizza sauce evenly on the base.
3. Add grated cheese and place basil leaves.
4. Sprinkle oregano and chili flakes, drizzle olive oil.
5. Bake for 12–15 mins or until cheese melts and crust turns golden.
6. Slice and serve hot.
"""
        Margherita_ingre='''Ingredients:
1 pizza base (store-bought or homemade)
1/2 cup pizza sauce
1 cup grated mozzarella cheese
Fresh basil leaves
1/2 tsp oregano, 1/2 tsp chili flakes
1 tbsp olive oil'''
        lines= Margherita.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\margherita.jpeg")
        img.show()         
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, Margherita_ingre)
            pdf.output("Margherita_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==4:
        Cheese="""Cheese Burst Pizza Recipe
Prep Time: 20 minutes
Cook Time: 15 minutes
Total Time: 35 minutes
Serves: 2 people
Ingredients:
2 pizza dough bases (one small, one medium)
1/2 cup mozzarella cheese (for stuffing)
1/2 cup pizza sauce
1 cup mozzarella cheese (for topping)
Oregano, chili flakes, basil, olive oil
Instructions:
1. Roll both doughs into thin rounds.
2. On the smaller one, spread stuffing cheese and cover with second base.
3. Seal edges well to trap cheese inside.
4. Spread pizza sauce on top, add topping cheese and seasonings.
5. Bake at 220°C for 12–15 mins until golden and bubbly.
6. Slice and enjoy the melty cheese burst!
"""
        Cheese_ingre='''Ingredients:
2 pizza dough bases (one small, one medium)
1/2 cup mozzarella cheese (for stuffing)
1/2 cup pizza sauce
1 cup mozzarella cheese (for topping)
Oregano, chili flakes, basil, olive oil'''
        lines= Cheese.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\cheese_pizza.jpeg")
        img.show()         
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, Cheese_ingre)
            pdf.output("Cheese_Brust_Pizza_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==5:
        Panna="""Panna Cotta Recipe
Prep Time: 10 minutes
Cook Time: 5 minutes
Chill Time: 4 hours
Total Time: 4 hrs 15 mins
Serves: 4 people
Ingredients:
1 cup fresh cream
1/2 cup milk
1/4 cup sugar
1 tsp vanilla extract
1 tsp gelatin (or agar agar)
2 tbsp water
Instructions:
1. Soak gelatin in 2 tbsp water for 5 minutes.
2. Heat cream, milk, and sugar in a pan. Do not boil.
3. Turn off heat, add soaked gelatin and mix well.
4. Add vanilla, stir until smooth.
5. Pour into molds and chill for 4 hours or until set.
6. Unmold and serve with fruit or sauce.
"""
        Panna_ingre='''Ingredients:
1 cup fresh cream
1/2 cup milk
1/4 cup sugar
1 tsp vanilla extract
1 tsp gelatin (or agar agar)
2 tbsp water'''
        lines=Panna.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\panna.jpg")
        img.show()         
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, Panna_ingre)
            pdf.output("Panna_Cotta_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==6:
        Tiramisu="""Tiramisu Recipe
Prep Time: 20 minutes
Chill Time: 4 to 6 hours
Total Time: 4 hrs 20 mins
Serves: 4 people
Ingredients:
12 ladyfinger biscuits
1/2 cup strong black coffee (cooled)
1 cup mascarpone cheese
1/2 cup whipping cream
1/4 cup powdered sugar
1 tsp vanilla extract
Cocoa powder for dusting
Instructions:
1. Beat cream with sugar and vanilla until soft peaks.
2. Fold in mascarpone gently to form a smooth mix.
3. Dip each biscuit briefly in coffee and layer in dish.
4. Spread half the cream mixture over biscuits.
5. Repeat with another biscuit layer and remaining cream.
6. Chill for 4–6 hrs. Dust with cocoa powder before serving.
"""
        Tiramisu_ingre='''Ingredients:
12 ladyfinger biscuits
1/2 cup strong black coffee (cooled)
1 cup mascarpone cheese
1/2 cup whipping cream
1/4 cup powdered sugar
1 tsp vanilla extract
Cocoa powder for dusting
 '''
        lines= Tiramisu.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\tiramisu.jpeg")
        img.show()         
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, Tiramisu_ingre)
            pdf.output("Tiramisu_ingredients.pdf")
            print('Downloaded Successfully !!!')   
        

    
    

from fpdf import FPDF
import pyttsx3
def mexican():
    print('''\n\n🍛 Rice & Sides

1. Mexican Rice
2. Nachos with Cheese 
-------
🌯 Main Course

3. Taco Bowl
4. Enchiladas
-------
🍮 Desserts

5. Churros
6. Tres Leches Cake 
-------''')
    ch=int(input("Choose the dish number you want to try:"))
    if ch==1:
        rice="""Mexican Rice Recipe
Prep Time: 10 minutes
Cook Time: 20 minutes
Total Time: 30 minutes
Serves: 2 to 3 people
Ingredients:
1 cup basmati or long-grain rice
1/2 cup chopped tomatoes
1/4 cup chopped onion
1 tsp chopped garlic
1/4 tsp cumin seeds, 1/2 tsp chili powder
1 tbsp tomato ketchup (optional)
2 tbsp oil, salt to taste, 2 cups water
Instructions:
1. Rinse and soak rice for 15 mins, then drain.
2. Heat oil, add cumin seeds and garlic, sauté till fragrant.
3. Add onions, cook till soft. Add tomatoes and cook until mushy.
4. Add chili powder, salt, ketchup, and mix well.
5. Add rice and water, bring to a boil.
6. Cover and simmer until rice is cooked and fluffy. Serve hot.
"""

        rice_ingre='''Ingredients:
1 cup basmati or long-grain rice
1/2 cup chopped tomatoes
1/4 cup chopped onion
1 tsp chopped garlic
1/4 tsp cumin seeds, 1/2 tsp chili powder
1 tbsp tomato ketchup (optional)
2 tbsp oil, salt to taste, 2 cups water'''
        # Split into words
        lines= rice.splitlines()

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
        img=Image.open("D:\\python\\receipe\\image\\friedrice.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10,rice_ingre)
            pdf.output("Mexcian_Rice_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==2:
        nachos="""Nachos with Cheese Recipe
Prep Time: 5 minutes
Cook Time: 10 minutes
Total Time: 15 minutes
Serves: 2 to 3 people
Ingredients:
1 packet plain tortilla chips (nachos)
1 cup grated cheese (cheddar or mozzarella)
1/4 cup chopped tomatoes
1/4 cup chopped onions
1 chopped green chili or jalapeños
1 tbsp tomato ketchup or salsa
Instructions:
1. Preheat oven to 180°C (350°F) or use stovetop.
2. Arrange tortilla chips on a plate or baking tray.
3. Sprinkle cheese evenly over the chips.
4. Add tomatoes, onions, chili or jalapeños on top.
5. Drizzle ketchup or salsa.
6. Bake or microwave until cheese melts. Serve hot.
"""
        nachos_ingre='''Ingredients:
1 cup mixed vegetables (carrot, bell pepper, beans)
1 tbsp Thai red curry paste
1 cup thick coconut milk
1/2 cup water
1 tsp soy sauce or fish sauce
1 tbsp oil
Salt to taste, fresh basil (optional)'''
        lines= nachos.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\nachoos.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, red_ingre)
            pdf.output("Nachos_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==3:
        taco="""Taco Bowl Recipe
Prep Time: 10 minutes
Cook Time: 15 minutes
Total Time: 25 minutes
Serves: 2 people
Ingredients:
1 cup cooked rice
1/2 cup cooked kidney beans (rajma) or black beans
1/4 cup chopped lettuce
1/4 cup chopped tomatoes
1/4 cup chopped onion
1/4 cup corn (boiled or grilled)
2 tbsp salsa or tomato ketchup
1/4 tsp chili powder, salt, pepper, lime juice
Instructions:
1. Season rice with salt, pepper, and lime. Keep aside.
2. Warm beans with chili powder and a pinch of salt.
3. In a bowl, layer rice, then beans, followed by veggies and corn.
4. Top with salsa and a squeeze of lime. Serve fresh.
"""
        taco_ingre='''Ingredients:
1 cup cooked rice
1/2 cup cooked kidney beans (rajma) or black beans
1/4 cup chopped lettuce
1/4 cup chopped tomatoes
1/4 cup chopped onion
1/4 cup corn (boiled or grilled)
2 tbsp salsa or tomato ketchup
1/4 tsp chili powder, salt, pepper, lime juice'''
        lines= taco.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\tacos.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, taco_ingre)
            pdf.output("Tacos_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==4:
        enchiladas="""Veg Enchiladas Recipe
Prep Time: 15 minutes
Cook Time: 20 minutes
Total Time: 35 minutes
Serves: 2 to 3 people
Ingredients:
4 small tortillas
1/2 cup cooked beans or paneer cubes
1/2 cup chopped veggies (onion, capsicum)
1/2 cup tomato puree
1/2 cup grated cheese
1 tsp chili powder, salt, oregano
1 tbsp oil
Instructions:
1. Heat oil, sauté veggies. Add beans, chili, salt. Mix well.
2. Fill tortillas with this mix, roll and place in greased baking dish.
3. Pour tomato puree over rolls, sprinkle cheese and oregano.
4. Bake at 180°C (350°F) for 15–20 mins until cheese melts.
5. Serve hot with salsa or sour cream.
"""
        enchiladas_ingre='''Ingredients:
4 small tortillas
1/2 cup cooked beans or paneer cubes
1/2 cup chopped veggies (onion, capsicum)
1/2 cup tomato puree
1/2 cup grated cheese
1 tsp chili powder, salt, oregano
1 tbsp oil'''
        lines= enchiladas.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\paneer.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, enchiladas_ingre)
            pdf.output("Enchiladas_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==5:
        churros="""Churros Recipe
Prep Time: 10 minutes
Cook Time: 15 minutes
Total Time: 25 minutes
Serves: 3 to 4 people
Ingredients:
1 cup water
2 tbsp sugar
2 tbsp butter
1 cup all-purpose flour
Oil for deep frying
1/4 cup sugar + 1 tsp cinnamon (for coating)
Instructions:
1. Boil water, sugar, and butter in a pan.
2. Add flour and stir until dough forms. Cool slightly.
3. Fill dough into piping bag with star nozzle.
4. Pipe into hot oil and fry until golden brown.
5. Roll fried churros in cinnamon sugar. Serve hot.
"""
        churros_ingre='''Ingredients:
1 cup water
2 tbsp sugar
2 tbsp butter
1 cup all-purpose flour
Oil for deep frying
1/4 cup sugar + 1 tsp cinnamon (for coating)'''
        lines=churros.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\enchiladas.jpeg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, churros_ingre)
            pdf.output("Churros_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==6:
        cake="""Tres Leches Cake Recipe
Prep Time: 15 minutes
Cook Time: 25 minutes
Chill Time: 4 hours
Total Time: 4 hrs 40 mins
Serves: 4 to 6 people
Ingredients:
1 cup all-purpose flour
1 tsp baking powder
3 eggs
1/2 cup sugar
1/3 cup milk
Mix of 1/2 cup condensed milk, 1/2 cup evaporated milk, 1/2 cup cream
Instructions:
1. Beat eggs and sugar until fluffy. Add milk and dry ingredients.
2. Pour into greased tin. Bake at 180°C for 25 minutes.
3. Poke holes in warm cake and pour milk mixture over it.
4. Chill for 4 hours. Top with whipped cream and serve.
"""

        cake_ingre='''Ingredients:
1 cup all-purpose flour
1 tsp baking powder
3 eggs
1/2 cup sugar
1/3 cup milk
Mix of 1/2 cup condensed milk, 1/2 cup evaporated milk, 1/2 cup cream
 '''
        lines= cake.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\Tres.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, cake_ingre)
            pdf.output("Tres_Leches_Cake_ingredients.pdf")
            print('Downloaded Successfully !!!')   
       

#mexican()    
    

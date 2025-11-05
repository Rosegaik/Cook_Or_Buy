from fpdf import FPDF
import pyttsx3
def korean():
    print('''🍚 Rice & Noodle Dishes

1. Bibimbap 
2. Kimchi Fried Rice 
-------
🥬 Vegetarian & Sides

3. Kimchi
4. Korean Potato Pancakes (Gamja Jeon)
-------
🧁 Desserts

5. Hotteok 
6. Bingsu
-------''')
    ch=int(input("Choose the dish number you want to try:"))
    if ch==1:
        Bibimbap="""Bibimbap Recipe
Prep Time: 15 minutes
Cook Time: 15 minutes
Total Time: 30 minutes
Serves: 2 people
Ingredients:
1 cup cooked rice
1/4 cup sautéed spinach
1/4 cup sautéed carrot (julienned)
1/4 cup sautéed zucchini
1/4 cup bean sprouts
1 fried egg
1 tbsp gochujang (Korean chili paste), 1 tsp sesame oil, sesame seeds
Instructions:
1. Cook rice and keep it warm in a bowl.
2. Sauté each veggie separately with little oil and salt.
3. Arrange veggies over the rice in sections.
4. Place fried egg on top, drizzle gochujang and sesame oil.
5. Sprinkle sesame seeds. Mix before eating.
"""

        Bibimbap_ingre='''Ingredients:
1 cup cooked rice
1/4 cup sautéed spinach
1/4 cup sautéed carrot (julienned)
1/4 cup sautéed zucchini
1/4 cup bean sprouts
1 fried egg
1 tbsp gochujang (Korean chili paste), 1 tsp sesame oil, sesame seeds'''
        # Split into words
        lines= Bibimbap.splitlines()

        # Text-to-speech setup
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)


        # Speak and show each word
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        Download=int(input("Do you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10,Bibimbap_ingre)
            pdf.output("Bibimbap_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==2:
        Kimchi="""Kimchi Fried Rice Recipe
Prep Time: 10 minutes
Cook Time: 10 minutes
Total Time: 20 minutes
Serves: 2 people
Ingredients:
1 cup cooked rice (preferably cold)
1/2 cup chopped kimchi
1 tbsp kimchi juice (optional)
1 tsp soy sauce
1 tsp sesame oil
1 tbsp oil
1 fried egg (optional), sesame seeds, chopped spring onion
Instructions:
1. Heat oil in a pan, sauté kimchi for 2 minutes.
2. Add rice, kimchi juice, soy sauce, and stir-fry well.
3. Drizzle sesame oil and mix evenly.
4. Top with fried egg, sesame seeds, and spring onions.
5. Serve hot.
"""
        Kimchi_ingre='''Ingredients:
1 cup cooked rice (preferably cold)
1/2 cup chopped kimchi
1 tbsp kimchi juice (optional)
1 tsp soy sauce
1 tsp sesame oil
1 tbsp oil
1 fried egg (optional), sesame seeds, chopped spring onion'''
        lines= Kimchi.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        Download=int(input("Do you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, Kimchi_ingre)
            pdf.output("Kimchi_Fried_Rice_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==3:
        kim="""Kimchi Recipe
Prep Time: 20 minutes
Rest Time: 6 to 24 hours
Total Time: 6 hrs+
Serves: Makes 1 medium jar
Ingredients:
1 small napa cabbage (cut into large pieces)
2 tbsp salt
2 tbsp red chili powder
1 tbsp ginger-garlic paste
1 tsp sugar
2 tbsp chopped spring onion
1 tbsp vinegar (optional)
Instructions:
1. Sprinkle salt on cabbage and let it rest 2 hours, then rinse and drain.
2. Mix chili powder, ginger-garlic, sugar, and vinegar into a paste.
3. Combine paste with cabbage and spring onion, mix well.
4. Store in a clean jar and press down to release liquid.
5. Leave at room temp for 6 to 24 hrs, then refrigerate.
"""
        kim_ingre='''Ingredients:
1 small napa cabbage (cut into large pieces)
2 tbsp salt
2 tbsp red chili powder
1 tbsp ginger-garlic paste
1 tsp sugar
2 tbsp chopped spring onion
1 tbsp vinegar (optional)'''
        lines= kim.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        Download=int(input("Do you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, kim_ingre)
            pdf.output("Kimichi_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==4:
        pancake="""Korean Potato Pancakes Recipe
Prep Time: 10 minutes
Cook Time: 10 minutes
Total Time: 20 minutes
Serves: 2 people
Ingredients:
2 medium potatoes, peeled
1 tbsp chopped spring onion (optional)
Salt to taste
Oil for frying
Instructions:
1. Grate potatoes and squeeze out excess water.
2. Add a pinch of salt and spring onion (if using).
3. Mix well to form a thick batter-like texture.
4. Heat oil in a pan, spoon batter into small round shapes.
5. Fry on medium heat until golden and crisp on both sides.
6. Serve hot with soy sauce or dipping sauce.
"""
        pancake_ingre='''Ingredients:
2 medium potatoes, peeled
1 tbsp chopped spring onion (optional)
Salt to taste
Oil for frying'''
        lines= pancake.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        Download=int(input("Do you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, pancake_ingre)
            pdf.output("Pancakes_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==5:
        hotteok="""Hotteok (Sweet Korean Pancakes) Recipe
Prep Time: 10 minutes
Rest Time: 1 hour
Cook Time: 10 minutes
Total Time: 1 hr 20 mins
Serves: 4 pancakes
Ingredients:
1 cup all-purpose flour
1/2 tsp yeast, 1 tsp sugar, pinch of salt
1/2 cup warm water
Filling: 2 tbsp brown sugar, 1 tbsp chopped nuts, 1/2 tsp cinnamon
Oil for frying
Instructions:
1. Mix flour, yeast, sugar, salt, and warm water into a dough.
2. Cover and let it rise for 1 hour.
3. Divide dough into 4 balls, flatten each and add filling inside.
4. Seal and flatten again gently.
5. Fry in a pan with oil until golden on both sides. Serve warm.
"""
        hotteok_ingre='''Ingredients:
1 cup all-purpose flour
1/2 tsp yeast, 1 tsp sugar, pinch of salt
1/2 cup warm water
Filling: 2 tbsp brown sugar, 1 tbsp chopped nuts, 1/2 tsp cinnamon
Oil for frying'''
        lines=hotteok.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        Download=int(input("Do you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, hotteok_ingre)
            pdf.output("Hotteok_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==6:
        Bingsu="""Bingsu (Korean Shaved Ice) Recipe
Prep Time: 10 minutes
Freeze Time: 4 hours
Total Time: 4 hrs 10 mins
Serves: 2 people
Ingredients:
1 cup milk or sweetened milk
1/4 cup sweetened condensed milk
1/2 cup chopped fruits (mango, strawberry, etc.)
2 tbsp red bean paste (optional)
Crushed ice or frozen milk
Toppings: ice cream, nuts, syrup
Instructions:
1. Freeze milk in a tray for 4 hours or until solid.
2. Crush or shave frozen milk finely (use a blender if needed).
3. Place shaved milk or ice in a bowl.
4. Top with fruits, red bean paste, condensed milk, and ice cream.
5. Serve immediately before it melts.
"""
        Bingsu_ingre='''Ingredients:
1 cup all-purpose flour
2 eggs
1/4 cup sugar
1 tbsp honey
1/2 tsp baking soda
1/3 cup water
Red bean paste (anko) for filling
 '''
        lines= Bingsu.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        Download=int(input("Do you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, Bingsu_ingre)
            pdf.output("Bingsu_ingredients.pdf")
            print('Downloaded Successfully !!!')   
       
#korean()
   
    

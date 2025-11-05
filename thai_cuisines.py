from fpdf import FPDF
import pyttsx3
def thai():
    print('''\n\n🍛 Thai Curries
1. Thai Green Curry 
2. Thai Red Curry 
-------
🍜 Noodles & Rice
3. Pad Thai 
4. Glass Noodle Salad 
-------
🧁 Thai Desserts
5. Sticky Rice with Mango
6. Thai Coconut Pudding 
-------''')
    ch=int(input("Choose the dish number you want to try:"))
    if ch==1:
        green="""Thai Green Curry Recipe
Prep Time: 10 minutes
Cook Time: 20 minutes
Total Time: 30 minutes
Serves: 2 to 3 people
Ingredients:
1 cup mixed vegetables (carrot, beans, capsicum)
1 tbsp Thai green curry paste
1 cup coconut milk
1/2 cup water
1 tsp soy sauce
1 tbsp oil
Salt to taste, fresh basil (optional)
Instructions:
1. Heat oil in a pan, add curry paste and sauté for 1 minute.
2. Add chopped vegetables and stir-fry for 2 to 3 minutes.
3. Pour in coconut milk and water, stir and bring to a boil.
4. Add soy sauce and salt. Simmer for 10–12 minutes.
5. Garnish with fresh basil and serve hot with jasmine rice.
"""

        green_ingre='''Ingredients:
1 cup mixed vegetables (carrot, beans, capsicum)
1 tbsp Thai green curry paste
1 cup coconut milk
1/2 cup water
1 tsp soy sauce
1 tbsp oil
Salt to taste, fresh basil (optional)'''
        # Split into words
        lines= green.splitlines()

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
        img=Image.open("D:\\python\\receipe\\image\\greencurry.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10,green_ingre)
            pdf.output("Green_Curry_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==2:
        red="""Thai Red Curry Recipe
Prep Time: 10 minutes
Cook Time: 20 minutes
Total Time: 30 minutes
Serves: 2 to 3 people
Ingredients:
1 cup mixed vegetables (carrot, bell pepper, beans)
1 tbsp Thai red curry paste
1 cup thick coconut milk
1/2 cup water
1 tsp soy sauce or fish sauce
1 tbsp oil
Salt to taste, fresh basil (optional)
Instructions:
1. Heat oil in a pan, add red curry paste, and sauté for 1 minute.
2. Add chopped vegetables and stir-fry for 2 to 3 minutes.
3. Add coconut milk and water. Stir well and bring to a boil.
4. Add soy or fish sauce and salt. Simmer for 10–12 minutes.
5. Garnish with fresh basil and serve hot with steamed rice.
"""
        red_ingre='''Ingredients:
1 cup mixed vegetables (carrot, bell pepper, beans)
1 tbsp Thai red curry paste
1 cup thick coconut milk
1/2 cup water
1 tsp soy sauce or fish sauce
1 tbsp oil
Salt to taste, fresh basil (optional)'''
        lines= red.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\redcurry.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, red_ingre)
            pdf.output("Red_Curry_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==3:
        pad="""Pad Thai Recipe
Prep Time: 10 minutes
Cook Time: 15 minutes
Total Time: 25 minutes
Serves: 2 people
Ingredients:
150g flat rice noodles
1/2 cup bean sprouts
1/4 cup chopped spring onion
1 egg (optional)
1 tbsp soy sauce, 1 tbsp tamarind pulp
1 tsp sugar, 1 tbsp oil
Chopped peanuts and lime wedges
Instructions:
1. Soak noodles in warm water for 10 mins and drain.
2. Heat oil in a pan, scramble the egg (if using).
3. Add noodles, tamarind pulp, soy sauce, and sugar. Toss well.
4. Add sprouts, spring onion, and stir-fry for 2 mins.
5. Serve hot topped with peanuts and lime wedges.
"""
        pad_ingre='''Ingredients:
150g flat rice noodles
1/2 cup bean sprouts
1/4 cup chopped spring onion
1 egg (optional)
1 tbsp soy sauce, 1 tbsp tamarind pulp
1 tsp sugar, 1 tbsp oil
Chopped peanuts and lime wedges'''
        lines= pad.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\pad.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, pad_ingre)
            pdf.output("Pad_Thai_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==4:
        glass="""Thai Glass Noodle Salad Recipe
Prep Time: 10 minutes
Cook Time: 5 minutes
Total Time: 15 minutes
Serves: 2 people
Ingredients:
1 cup glass noodles (mung bean vermicelli)
1/4 cup chopped onion
1/4 cup grated carrot
1/4 cup chopped cucumber
1 tbsp lime juice
1 tsp soy sauce
1 tsp chili flakes, salt to taste
Instructions:
1. Soak glass noodles in hot water for 5 mins, then drain.
2. In a bowl, mix lime juice, soy sauce, chili flakes, and salt.
3. Add noodles, onion, carrot, and cucumber.
4. Toss everything well to coat with dressing.
5. Chill briefly and serve fresh as a salad or side.
"""
        glass_ingre='''Ingredients:
1 cup glass noodles (mung bean vermicelli)
1/4 cup chopped onion
1/4 cup grated carrot
1/4 cup chopped cucumber
1 tbsp lime juice
1 tsp soy sauce
1 tsp chili flakes, salt to taste'''
        lines= glass.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\glass.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, glass_ingre)
            pdf.output("Glass_Noodles_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==5:
        sticky="""Sticky Rice with Mango Recipe
Prep Time: 10 minutes
Cook Time: 20 minutes
Total Time: 30 minutes
Serves: 2 people
Ingredients:
1/2 cup glutinous (sticky) rice
1/2 cup coconut milk
1/4 cup sugar
1/8 tsp salt
1 ripe mango, sliced
1 tsp sesame seeds (optional)
Instructions:
1. Soak sticky rice for 3–4 hrs, then steam or boil until soft.
2. Heat coconut milk, sugar, and salt. Do not boil.
3. Pour warm coconut milk over cooked rice. Let it soak 10 mins.
4. Serve rice topped with mango slices.
5. Sprinkle sesame seeds if desired. Serve warm or chilled.
"""
        sticky_ingre='''Ingredients:
1/2 cup glutinous (sticky) rice
1/2 cup coconut milk
1/4 cup sugar
1/8 tsp salt
1 ripe mango, sliced
1 tsp sesame seeds (optional)'''
        lines=sticky.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\mangorice.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, sticky_ingre)
            pdf.output("Sticky_Rice_With_Mango_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==6:
        pudding="""Thai Coconut Pudding Recipe
Prep Time: 10 minutes
Cook Time: 10 minutes
Chill Time: 2 hours
Total Time: 2 hrs 20 mins
Serves: 3 to 4 people
Ingredients:
1 cup coconut milk
1/2 cup water
1/4 cup sugar
1/4 cup corn flour or rice flour
1/8 tsp salt
Instructions:
1. Mix coconut milk, water, sugar, flour, and salt in a pan.
2. Cook on low flame, stirring constantly.
3. Stir until it thickens and turns glossy.
4. Pour into small cups or bowls and cool.
5. Chill for 2 hours and serve cold.
"""
        pudding_ingre='''Ingredients:
1 cup coconut milk
1/2 cup water
1/4 cup sugar
1/4 cup corn flour or rice flour
1/8 tsp salt
 '''
        lines= pudding.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\pudding.jpeg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, pudding_ingre)
            pdf.output("Coconut_pudding_ingredients.pdf")
            print('Downloaded Successfully !!!')   
       

    
    

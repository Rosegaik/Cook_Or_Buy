from fpdf import FPDF
import pyttsx3
def chinese():
    print('''\n\n🍝 Noodles & Rice:
1.Schezwan Noodles
2.Schezwan Fried Rice
-------
🧆 Starters:
3.Gobi Manchurian
4.Paneer chilli
-------
🍲 Soups:
5.Manchow Soup
6.Sweet Corn Soup
-------''')
    ch=int(input("\nChoose the dish number you want to try:"))
    if ch==1:
        noodles="""Schezwan Noodles Recipe

Prep Time: 10 minutes
Cook Time: 15 minutes
Total Time: 25 minutes
Serves: 2 to 3 people

Ingredients:
150g noodles
1/2 cup sliced capsicum
1/2 cup shredded cabbage
1/4 cup carrots (julienned)
1 tbsp chopped garlic
2 to 3 tbsp Schezwan sauce
1 tsp soy sauce
Salt to taste
2 tbsp oil

Instructions:
1. Boil noodles, drain and rinse with cold water. Keep aside.
2. Heat oil in a wok or pan. Add garlic and sauté for a few seconds.
3. Add carrots, cabbage, and capsicum. Stir-fry on high flame for 2 minutes.
4. Add Schezwan sauce, soy sauce, and salt. Mix well.
5. Add the cooked noodles and toss everything together until well combined.
6. Serve hot with chili vinegar or Manchurian.
"""
        noodles_ingre='''Ingredients:
150g noodles
1/2 cup sliced capsicum
1/2 cup shredded cabbage
1/4 cup carrots (julienned)
1 tbsp chopped garlic
2 to 3 tbsp Schezwan sauce
1 tsp soy sauce
Salt to taste
2 tbsp oil'''
        # Split into words
        lines= noodles.splitlines()

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
        img=Image.open("D:\\python\\receipe\\image\\noodles.jpg")
        img.show()         
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10,noodles_ingre)
            pdf.output("Schezwan_Noodles_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==2:
        fried="""Schezwan Fried Rice Recipe

Prep Time: 10 minutes
Cook Time: 15 minutes
Total Time: 25 minutes
Serves: 2 to 3 people

Ingredients:
2 cups cooked and cooled rice
1/2 cup chopped capsicum
1/4 cup chopped carrots
1/4 cup shredded cabbage
1 tbsp chopped garlic
2 to 3 tbsp Schezwan sauce
1 tsp soy sauce, salt to taste
2 tbsp oil

Instructions:
1. Heat oil in a wok. Add garlic and sauté for a few seconds.
2. Add all vegetables and stir-fry on high flame for 2 to 3 minutes.
3. Add Schezwan sauce, soy sauce, and salt. Mix well.
4. Add cooked rice and toss everything on high heat until combined.
5. Serve hot with Manchurian or chili paneer.
"""
        fried_ingre='''Ingredients:
2 cups cooked and cooled rice
1/2 cup chopped capsicum
1/4 cup chopped carrots
1/4 cup shredded cabbage
1 tbsp chopped garlic
2 to 3 tbsp Schezwan sauce
1 tsp soy sauce, salt to taste
2 tbsp oil'''
        lines= fried.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
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
            pdf.multi_cell(0, 10, fried_ingre)
            pdf.output("Schezwan_Fried_Rice_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==3:
        gobi="""Gobi Manchurian Recipe
Prep Time: 10 minutes
Cook Time: 15 minutes
Total Time: 25 minutes
Serves: 2 to 3 people
Ingredients:
2 cups cauliflower florets
1/4 cup maida, 1/4 cup corn flour
1/2 tsp red chili powder, salt to taste
1/2 tsp ginger garlic paste
1/4 cup chopped onion, 1/4 cup capsicum
1 tbsp soy sauce, 1 tbsp tomato ketchup
Oil to deep fry
Instructions:
1. Boil cauliflower for 3 mins, drain completely.
2. Mix maida, corn flour, salt, chili, water to make thick batter.
3. Dip florets, coat well, deep fry till golden and crisp.
4. Heat oil, sauté onion, capsicum, and ginger-garlic paste.
5. Add sauces and fried florets, toss well.
6. Serve hot as starter or side dish.
"""
        gobi_ingre='''Ingredients:
2 cups cauliflower florets
1/4 cup maida, 1/4 cup corn flour
1/2 tsp red chili powder, salt to taste
1/2 tsp ginger garlic paste
1/4 cup chopped onion, 1/4 cup capsicum
1 tbsp soy sauce, 1 tbsp tomato ketchup
Oil to deep fry'''
        lines= gobi.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\gobi.jpeg")
        img.show()         
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, gobi_ingre)
            pdf.output("Gobi_Manchurian_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==4:
        chilli="""Paneer Chilli Recipe
Prep Time: 10 minutes
Cook Time: 15 minutes
Total Time: 25 minutes
Serves: 2 to 3 people
Ingredients:
200g paneer cubes
1/4 cup corn flour, salt, pepper
1/4 cup chopped onion, 1/4 cup capsicum
1 tbsp chopped garlic
1 tbsp soy sauce, 1 tbsp chili sauce, 1 tbsp ketchup
Oil to shallow fry
Instructions:
1. Toss paneer with corn flour, salt, pepper. Shallow fry till golden.
2. In pan, heat oil and sauté garlic for few seconds.
3. Add onion and capsicum, stir-fry 1 to 2 minutes on high flame.
4. Add all sauces, mix well.
5. Add fried paneer and toss until coated.
6. Serve hot as dry starter or side.
"""
        chilli_ingre='''Ingredients:
200g paneer cubes
1/4 cup corn flour, salt, pepper
1/4 cup chopped onion, 1/4 cup capsicum
1 tbsp chopped garlic
1 tbsp soy sauce, 1 tbsp chili sauce, 1 tbsp ketchup
Oil to shallow fry '''
        lines= chilli.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\chilli.jpg")
        img.show()         
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, chilli_ingre)
            pdf.output("Chilli_Chicken_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==5:
        manchow="""Manchow Soup Recipe
Prep Time: 10 minutes
Cook Time: 15 minutes
Total Time: 25 minutes
Serves: 2 to 3 people
Ingredients:
1/4 cup chopped cabbage
1/4 cup chopped carrot
1/4 cup chopped capsicum
1 tbsp chopped garlic, 1 tsp chopped ginger
1 tbsp soy sauce, 1 tsp chili sauce, 1 tsp vinegar
1 tbsp corn flour mixed in 2 tbsp water
2 cups water or veg stock, salt and pepper to taste
Instructions:
1. Heat oil, sauté garlic and ginger for 30 seconds.
2. Add all vegetables and stir-fry on high flame for 2 minutes.
3. Add water, sauces, salt, and pepper. Let it boil.
4. Stir in corn flour slurry and cook till slightly thickened.
5. Serve hot topped with crispy fried noodles.
"""
        manchow_ingre='''Ingredients:
1/4 cup chopped cabbage
1/4 cup chopped carrot
1/4 cup chopped capsicum
1 tbsp chopped garlic, 1 tsp chopped ginger
1 tbsp soy sauce, 1 tsp chili sauce, 1 tsp vinegar
1 tbsp corn flour mixed in 2 tbsp water
2 cups water or veg stock, salt and pepper to taste '''
        lines= manchow.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\manchow.jpg")
        img.show()         
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, manchow_ingre)
            pdf.output("Manchow_Soup_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==6:
        corn="""Sweet Corn Soup Recipe
Prep Time: 10 minutes
Cook Time: 15 minutes
Total Time: 25 minutes
Serves: 2 to 3 people
Ingredients:
1/2 cup sweet corn kernels
1 tbsp chopped carrot
1 tbsp chopped beans
2 cups water or veg stock
1 tbsp corn flour mixed in 2 tbsp water
Salt and pepper to taste
Instructions:
1. Blend half of the sweet corn into a coarse paste.
2. Boil water, add whole corn, paste, and chopped veggies.
3. Cook for 5 to 6 minutes until veggies soften.
4. Add corn flour slurry, stir and simmer till slightly thick.
5. Add salt and pepper. Serve hot.
"""
        corn_ingre='''Ingredients:
1/2 cup sweet corn kernels
1 tbsp chopped carrot
1 tbsp chopped beans
2 cups water or veg stock
1 tbsp corn flour mixed in 2 tbsp water
Salt and pepper to taste
 '''
        lines= corn.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\corn.jpg")
        img.show()         
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, corn_ingre)
            pdf.output("Sweet_Corn_ingredients.pdf")
            print('Downloaded Successfully !!!')
    

    




       

    
    

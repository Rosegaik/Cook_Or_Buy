from fpdf import FPDF
import pyttsx3
def japanese():
    print('''\n\n🍱 Main Dishes

1. Teriyaki Chicken 
2. Katsu Curry 
-------
🍜 Noodles

3. Ramen 
4. Udon 
-------
🧁 Desserts

5. Mochi 
6. Dorayaki 
-------''')
    ch=int(input("Choose the dish number you want to try:"))
    if ch==1:
        Teriyaki="""Teriyaki Chicken Recipe
Prep Time: 10 minutes
Cook Time: 15 minutes
Total Time: 25 minutes
Serves: 2 people
Ingredients:
200g boneless chicken (thigh or breast)
2 tbsp soy sauce
1 tbsp honey or sugar
1 tbsp mirin (or vinegar)
1 tsp ginger-garlic paste
1 tbsp oil, sesame seeds, spring onion
Instructions:
1. Mix soy sauce, honey, mirin, and ginger-garlic to make sauce.
2. Heat oil in a pan, cook chicken until golden on both sides.
3. Pour sauce over chicken, cook on low until thick and glazed.
4. Slice chicken, garnish with sesame seeds and spring onion.
5. Serve with steamed rice or noodles.
"""

        Teriyaki_ingre='''Ingredients:
200g boneless chicken (thigh or breast)
2 tbsp soy sauce
1 tbsp honey or sugar
1 tbsp mirin (or vinegar)
1 tsp ginger-garlic paste
1 tbsp oil, sesame seeds, spring onion'''
        # Split into words
        lines= Teriyaki.splitlines()

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
        img=Image.open("D:\\python\\receipe\\image\\Teriyaki.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10,Teriyaki_ingre)
            pdf.output("Teriyaki_Rice_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==2:
        Katsu="""Katsu Curry Recipe
Prep Time: 15 minutes
Cook Time: 25 minutes
Total Time: 40 minutes
Serves: 2 people
Ingredients:
2 chicken breasts or cutlets
1/2 cup breadcrumbs, 1/4 cup flour, 1 egg
1 tbsp oil, salt, pepper
For curry: 1 chopped onion, 1 chopped carrot, 1 tbsp curry powder
1 cup water, 1 tbsp flour, 1 tbsp soy sauce
Instructions:
1. Season chicken, coat with flour, dip in egg, then breadcrumbs.
2. Pan-fry until golden and cooked through.
3. For curry, sauté onion and carrot in oil until soft.
4. Add curry powder, flour, soy sauce, and water. Simmer 10 mins.
5. Slice chicken and serve over rice with curry sauce.
"""
        Katsu_ingre='''Ingredients:
2 chicken breasts or cutlets
1/2 cup breadcrumbs, 1/4 cup flour, 1 egg
1 tbsp oil, salt, pepper
For curry: 1 chopped onion, 1 chopped carrot, 1 tbsp curry powder
1 cup water, 1 tbsp flour, 1 tbsp soy sauce'''
        lines= Katsu.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\katsu.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, Katsu_ingre)
            pdf.output("Katsu_Curry_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==3:
        ramen="""Ramen Recipe
Prep Time: 10 minutes
Cook Time: 15 minutes
Total Time: 25 minutes
Serves: 2 people
Ingredients:
2 packs ramen noodles
3 cups vegetable or chicken broth
1 tbsp soy sauce, 1 tsp sesame oil
1/2 tsp ginger-garlic paste
1/4 cup chopped spring onion
Toppings: boiled egg, corn, mushrooms, spinach
Instructions:
1. Heat broth, add soy sauce, sesame oil, and ginger-garlic.
2. Simmer for 5 minutes to infuse flavor.
3. Add ramen noodles and cook as per packet instructions.
4. Pour into bowls, top with egg, veggies, and spring onions.
5. Serve hot.
"""
        ramen_ingre='''Ingredients:
2 packs ramen noodles
3 cups vegetable or chicken broth
1 tbsp soy sauce, 1 tsp sesame oil
1/2 tsp ginger-garlic paste
1/4 cup chopped spring onion
Toppings: boiled egg, corn, mushrooms, spinach'''
        lines= ramen.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\ramen.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, ramen_ingre)
            pdf.output("Ramen_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==4:
        udon="""Udon Noodle Soup Recipe
Prep Time: 10 minutes
Cook Time: 15 minutes
Total Time: 25 minutes
Serves: 2 people
Ingredients:
200g udon noodles (fresh or frozen)
3 cups vegetable or dashi broth
1 tbsp soy sauce, 1 tsp mirin (or vinegar)
1/2 tsp sugar
1/4 cup sliced mushrooms
Chopped spring onion, spinach, sesame seeds
Instructions:
1. Heat broth, add soy sauce, mirin, and sugar.
2. Add mushrooms and simmer for 5 minutes.
3. Cook udon noodles separately if needed.
4. Add noodles to the broth and heat through.
5. Serve in bowls with spinach, spring onions, and sesame.
"""
        udon_ingre='''Ingredients:
200g udon noodles (fresh or frozen)
3 cups vegetable or dashi broth
1 tbsp soy sauce, 1 tsp mirin (or vinegar)
1/2 tsp sugar
1/4 cup sliced mushrooms
Chopped spring onion, spinach, sesame seeds'''
        lines= udon.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\udon.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, udon_ingre)
            pdf.output("Udon_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==5:
        mochi="""Mochi Recipe
Prep Time: 10 minutes
Cook Time: 10 minutes
Total Time: 20 minutes
Serves: 6 small mochi
Ingredients:
1 cup glutinous rice flour (mochiko)
3/4 cup water
1/4 cup sugar
Cornstarch for dusting
Optional filling: red bean paste or chocolate
Instructions:
1. Mix rice flour, sugar, and water in a microwave-safe bowl.
2. Cover and microwave for 2–3 minutes, stirring halfway.
3. When thick and sticky, let it cool slightly.
4. Dust surface with cornstarch and place dough on it.
5. Divide, flatten, and fill with paste or chocolate if using.
6. Seal and shape into balls. Serve or chill.
"""
        mochi_ingre='''Ingredients:
1 cup glutinous rice flour (mochiko)
3/4 cup water
1/4 cup sugar
Cornstarch for dusting
Optional filling: red bean paste or chocolate'''
        lines=mochi.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\mochi.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, macho_ingre)
            pdf.output("Macho_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==6:
        dorayaki="""Dorayaki Recipe
Prep Time: 10 minutes
Cook Time: 15 minutes
Total Time: 25 minutes
Serves: 4 pancakes (2 sandwiches)
Ingredients:
1 cup all-purpose flour
2 eggs
1/4 cup sugar
1 tbsp honey
1/2 tsp baking soda
1/3 cup water
Red bean paste (anko) for filling
Instructions:
1. Mix eggs, sugar, honey, and baking soda in a bowl.
2. Add flour and water gradually to make smooth batter.
3. Let it rest for 10 minutes.
4. Cook small round pancakes on a nonstick pan.
5. Sandwich red bean paste between two pancakes and serve.
"""
        dorayaki_ingre='''Ingredients:
1 cup all-purpose flour
2 eggs
1/4 cup sugar
1 tbsp honey
1/2 tsp baking soda
1/3 cup water
Red bean paste (anko) for filling
 '''
        lines= dorayaki.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\dorayaki.jpg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, dorayaki_ingre)
            pdf.output("Dorayaki_ingredients.pdf")
            print('Downloaded Successfully !!!')   
       

#japanese()    
    

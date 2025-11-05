
from fpdf import FPDF
import pyttsx3
def indian():
    print('''\n\n🍛 Main Course(Gravy & Curry:
1.Paneer butter masala
2.Pulikolambu
-------
🍽🫓 Indian Breads:
3.Naan
4.Poori
-------
🍚 Rice Dishes:
5.Jeera rice
6.Sambar rice
-------
🧆 Snacks & Starters:
7.Aloo Tikki
8.Medu Vada
-------''')
    ch=int(input("Choose the dish number you want to try:"))
    if ch==1:
        paneer="""Paneer Butter Masala Recipe

Prep Time: 10 minutes
Cook Time: 20 minutes
Total Time: 30 minutes
Serves: 3 to 4 people

Ingredients:
200 grams paneer (cubed)
2 large tomatoes (chopped)
1 onion (chopped)
1 tbsp ginger garlic paste
2 tbsp butter
1 tbsp oil
1/2 tsp cumin seeds
1/2 tsp turmeric powder
1 tsp red chili powder
1 tsp garam masala
1 tbsp coriander powder
2 tbsp fresh cream
10 cashew nuts (soaked)
Salt to taste
Water as needed
Kasuri methi – a pinch

Instructions:
1. Blend tomatoes and soaked cashews into a smooth paste.
2. Heat oil and butter in a pan. Add cumin seeds.
3. Add chopped onion and sauté till golden.
4. Add ginger garlic paste, sauté till raw smell goes.
5. Add tomato-cashew paste and cook till oil separates.
6. Add turmeric, chili powder, coriander powder, and salt.
7. Cook till masala thickens and darkens.
8. Add water for gravy consistency and paneer cubes.
9. Simmer for 5 minutes. Add cream and garam masala.
10. Crush kasuri methi and mix in. Cook 2 minutes.
11. Serve hot with roti, naan, or rice.
"""
        paneer_ingre='''Ingredients:
200 grams paneer (cubed)
2 large tomatoes (chopped)
1 onion (chopped)
1 tbsp ginger garlic paste
2 tbsp butter
1 tbsp oil
1/2 tsp cumin seeds
1/2 tsp turmeric powder
1 tsp red chili powder
1 tsp garam masala
1 tbsp coriander powder
2 tbsp fresh cream
10 cashew nuts (soaked)
Salt to taste
Water as needed
Kasuri methi  a pinch'''


        #print(paneer)
        # Split into words
        lines= paneer.splitlines()

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
        img=Image.open("D:\\python\\receipe\\image\\paneer.jpg")
        img.show()
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No:"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, paneer_ingre)
            pdf.output("Panner_ingredients.pdf")
            print('Downloaded Successfully !!!')
  
    elif ch==2:
        puzi="""Puli Kulambu (Tamarind Curry) Recipe
Prep Time: 10 minutes
Cook Time: 20 minutes
Total Time: 30 minutes
Serves: 3 to 4 people

Ingredients:
Lemon-sized tamarind (soaked)
1.5 tbsp sambar/kulambu powder
1/2 tsp turmeric powder
1/2 tsp mustard seeds
1/2 tsp fenugreek seeds
1/4 tsp asafoetida (hing)
1–2 dry red chilies
1 sprig curry leaves
1 small onion or shallots, chopped
1–2 garlic cloves, crushed (optional)
1–2 tbsp sesame oil (nallennai)
Salt as needed
1 to 1.5 cups water

Instructions:
1. Soak tamarind in warm water and extract juice.
2. Heat sesame oil in a pan.
3. Add mustard seeds and let them splutter.
4. Add fenugreek, red chilies, curry leaves, and asafoetida.
5. Add onions and garlic, sauté till golden.
6. Add vegetables and cook for 2 minutes.
7. Add turmeric and kuzhambu powder, mix well.
8. Pour in tamarind extract and water.
9. Add salt and boil for 15–20 minutes.
10. Cook till oil separates and gravy thickens.
11. Serve hot with rice and papad.
"""
        puzi_ingre='''Puzhi Kuzhambu (Tamarind Curry)

Ingredients:
Lemon sized tamarind (soaked)
2 tbsp sambar/kuzhambu powder
1/2 tsp turmeric powder
1/2 tsp mustard seeds
1/2 tsp fenugreek seeds
1/4 tsp asafoetida (hing)
2 dry red chilies
1 sprig curry leaves
1 small onion or shallots (chopped)
1 to 2 garlic cloves crushed (optional)
1 to 2 tbsp sesame oil (nallennai)
Salt as needed
1 to 2 cups water'''
        lines= puzi.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        

        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\pulikolambu.jpeg")
        img.show()        
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, puzi_ingre)
            pdf.output("Puzikolambu_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==3:
        naan='''Naan Recipe

Prep Time: 15 minutes (+1 hour rest)
Cook Time: 10 minutes
Total Time: 25 minutes (+resting)
Serves: 3 to 4 people

Ingredients:
1 cup all purpose flour
1/4 tsp baking powder
1/4 tsp baking soda
1/4 cup curd
1/4 tsp salt
Warm water as needed
1 tsp sugar
1 tsp oil or butter

Instructions:
1. Mix flour, salt, baking powder, baking soda, and sugar.
2. Add curd and little warm water to form a soft dough.
3. Knead well and rest the dough for 1 hour.
4. Roll small portions into oval shapes.
5. Cook on hot tawa or pan until bubbles appear.
6. Flip and cook other side. Apply butter and serve hot.
'''
        naan_ingre='''Ingredients:
1 cup all purpose flour
1/4 tsp baking powder
1/4 tsp baking soda
1/4 cup curd
1/4 tsp salt
Warm water as needed
1 tsp sugar
1 tsp oil or butter'''
        lines= naan.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\naan.jpg")
        img.show()         

        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, naan_ingre)
            pdf.output("Naan_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==4:
        poori='''Poori Recipe

Prep Time: 10 minutes
Cook Time: 15 minutes
Total Time: 25 minutes
Serves: 3 to 4 people

Ingredients:
1 cup whole wheat flour
1/4 tsp salt
Water as needed
1 tsp oil (for dough)
Oil for deep frying

Instructions:
1. Mix flour, salt, and a tsp of oil in a bowl.
2. Add water gradually and knead into a stiff dough.
3. Rest the dough for 10 minutes.
4. Divide into small balls and roll into small circles.
5. Heat oil in a deep pan until hot.
6. Fry pooris one at a time, pressing gently to puff up.
7. Flip and cook both sides until golden.
8. Drain excess oil and serve hot with curry or chutney.
 '''
        poori_ingre='''Ingredients:
1 cup whole wheat flour
1/4 tsp salt
Water as needed
1 tsp oil (for dough)
Oil for deep frying '''
        
        lines= poori.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\poori.jpeg")
        img.show()         
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, poori_ingre)
            pdf.output("Poori_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==5:
        jeera='''Jeera Rice Recipe

Prep Time: 5 minutes
Cook Time: 15 minutes
Total Time: 20 minutes
Serves: 2 to 3 people

Ingredients:
1 cup basmati rice
2 cups water
1 tbsp ghee or oil
1 tsp cumin seeds
Salt to taste

Instructions:
1. Rinse and soak rice for 15 minutes, then drain.
2. Heat ghee in a pan, add cumin seeds and let them splutter.
3. Add rice, salt, and water. Bring to a boil.
4. Cover and simmer on low flame till rice is cooked.
5. Fluff gently and serve hot with dal or curry.
'''
        jeera_ingre='''Ingredients:
1 cup basmati rice
2 cups water
1 tbsp ghee or oil
1 tsp cumin seeds
Salt to taste '''
        lines= jeera.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\jeerarice.jpg")
        img.show()         
        Download=int(input("Do you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, jeera_ingre)
            pdf.output("jeera_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==6:
        sambar="""Sambar Rice Recipe

Prep Time: 10 minutes
Cook Time: 20 minutes
Total Time: 30 minutes
Serves: 3 to 4 people

Ingredients:
1/2 cup toor dal
1/2 cup rice
1 onion, 1 tomato, few vegetables (carrot, beans)
1 tsp sambar powder, 1/4 tsp turmeric, salt
1 tbsp tamarind extract
1 tsp mustard seeds, curry leaves, dried chili, hing
1 tbsp oil or ghee

Instructions:
1. Pressure cook dal and rice together with turmeric.
2. Heat oil, add mustard seeds, curry leaves, chili, and hing.
3. Add onions, tomatoes, chopped veggies, and sauté.
4. Add sambar powder, tamarind, salt, and little water.
5. Cook till veggies soften, then add mashed dal-rice.
6. Mix well, simmer for 5 mins, serve hot with pickle/papad.
"""
        sambar_ingre='''Ingredients:
1/2 cup toor dal
1/2 cup rice
1 onion, 1 tomato, few vegetables (carrot, beans)
1 tsp sambar powder, 1/4 tsp turmeric, salt
1 tbsp tamarind extract
1 tsp mustard seeds, curry leaves, dried chili, hing
1 tbsp oil or ghee
 '''
        lines= sambar.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\sambarrice.jpg")
        img.show()         
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, sambar_ingre)
            pdf.output("sambar_rice_ingredients.pdf")
            print('Downloaded Successfully !!!')
    

    elif ch==7:
        aloo='''Aloo Tikki Recipe

Prep Time: 10 minutes
Cook Time: 10 minutes
Total Time: 20 minutes
Serves: 2 to 3 people

Ingredients:
3 boiled potatoes
1 tsp red chili powder
1/2 tsp garam masala
1 tbsp corn flour or bread crumbs
Salt to taste
Oil for shallow frying

Instructions:
1. Mash potatoes and mix with spices, salt, and corn flour.
2. Shape into flat round tikkis.
3. Heat oil on tawa, shallow fry tikkis till golden brown.
4. Serve hot with green chutney or ketchup.
 '''
        aloo_ingre='''Ingredients:
3 boiled potatoes
1 tsp red chili powder
1/2 tsp garam masala
1 tbsp corn flour or bread crumbs
Salt to taste
Oil for shallow frying '''
        lines= aloo.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\alootikki.jpg")
        img.show()         
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, aloo_ingre)
            pdf.output("Aloo_Tikki_ingredients.pdf")
            print('Downloaded Successfully !!!')
    elif ch==8:
        medu='''Medu Vada Recipe

Prep Time: 10 minutes (+3 hrs soaking)
Cook Time: 15 minutes
Total Time: 25 minutes (+soaking)
Serves: 3 to 4 people

Ingredients:
1 cup urad dal (soaked 3 hours)
1 tsp chopped ginger
2 chopped green chilies
Few curry leaves, salt, oil to fry

Instructions:
1. Grind soaked dal into a thick, fluffy batter.
2. Add salt, ginger, chilies, and curry leaves. Mix well.
3. Wet hands, shape into doughnut-style vadas.
4. Deep fry in hot oil till golden and crisp.
5. Serve hot with coconut chutney or sambar.
'''
        medu_ingre='''Ingredients:
1 cup urad dal (soaked 3 hours)
1 tsp chopped ginger
2 chopped green chilies
Few curry leaves, salt, oil to fry '''
        lines= medu.splitlines()
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        for line in lines:
            if line.strip():
                print("👉", line)
                engine.say(line)
                engine.runAndWait()
        from PIL import Image
        img=Image.open("D:\\python\\receipe\\image\\meduvada.jpg")
        img.show()         
        Download=int(input("\nDo you want to download this ingredients enter 1 for Yes, 0 for No"))
        if Download==1:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, medu_ingre)
            pdf.output("Medu_Vada_ingredients.pdf")
            print('Downloaded Successfully !!!')
    
#indian()            
        
 



        
      

    
    

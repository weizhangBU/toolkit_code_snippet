q14 = pd.DataFrame(data={"recipe": ["cake", "cake", "cake", "cake", "candy", "candy"],
                         "ingredient": ["flour", "water", "sugar", "butter", "sugar", "water"],
                         "cups": [2, 0.5, 1, 0.25, 2, 1]})

p14 = q14.pivot_table(index='recipe', columns='ingredient', values='cups', aggfunc='sum', fill_value=0)

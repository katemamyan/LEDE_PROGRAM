# requests_cache lib

#library/packege
#https://www.youtube.com/watch?v=4Fdyft-ky0w 


#%%
art_pieces = [
     { 'title': 'Gold Star', 'year': 1805, "price" : 8039 },
     { 'title': 'Blunderbuss', 'year': 1800, "price" : 333 },
     { 'title': 'Chairlift', 'year': 1976, "price" : 232 },
     { 'title': 'Rancor', 'year': 2002, "price" : 4777 },
]
#%%
len(art_pieces)
# %%
count = 0

for piece in art_pieces:
    if piece['price'] > 1000:
        count = count + 1

print(f"You have {count} pieces that are expensive")
# %%
prices = [piece['price'] for piece in art_pieces]
max(prices)
# %%
prices = [piece['price'] for piece in art_pieces if piece['year'] > 1900]
sum(prices)
# %%

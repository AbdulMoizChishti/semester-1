favorite_places= {'Moiz': ['Niagra Fall', 'Dream World', 'Maldives']
,'\nShaheer': ['Tibetan plateau','Taj Mahal' ,'badshahi masjid']
,'\nTalal': ['Burj Khalifa', 'Eifel tower', 'Devils Point']}
for names, places in favorite_places.items():
 print(names, " likes the following places:") 
 for place in places:
     print("- " , place) 
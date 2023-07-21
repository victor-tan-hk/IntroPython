

animals = ['cat','dog','rat','mouse','elephant','chicken','horse']

#initial write
with open('animals.txt', 'w') as f:
    #Need to add the \n to start each list item on a new line
    #in the file
    f.write('\n'.join(animals))

#appending additional content
#comment out first

# more_animals = ['lion','cheetah','zebra','leopard']
# with open('animals.txt', 'a') as f:
#     f.write('\n'.join(more_animals)) 

quote = '成功を収める人とは人が投げてきたレンガでしっかりした基盤を築くことができる人のことである。'
with open('japanese.txt', 'w', encoding='utf-8') as f:
    f.write(quote)

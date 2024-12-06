d={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
sum=0
while True:
    try:
        item=input('Item: ')
        for i in d:
            if i.lower()==item.lower():
                sum+=d[i]
                print('$',"{:.2f}".format(sum),sep='')
            else:
                continue
    except ValueError:
        pass
    except EOFError:
        break
    except KeyError:
        pass

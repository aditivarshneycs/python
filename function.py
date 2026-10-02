# num=int(input("enter number: "))

# def even_num(num):
#     if num % 2 == 0:
#         print("even number")
#     else:
#         print("odd number")


# even_num(num)

def flexi(*number):
    product=1
    for i in number:
        product=product*i
    print(product)


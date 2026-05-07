print("==================Area Calculator 📐==================")
height=0
base=0
lenght=0
width=0
side=0
radius=0
while True:
    choice=int(input("\n1. Triangle\n2. Rectangle\n3. Square\n4. Circle\n5. Quit\n\n Which Shape: "))

    if choice==1:
        height=float(input("Height: "))
        base=float(input("Base: "))
        area_Triangle=(height*base)/2
        print(f"The area is {area_Triangle}")
       
        
    elif choice==2:
        lenght=float(input("Lenght: "))
        width=float(input("Width: "))
        area_Rectangle=lenght*width
        print(f"The area is {area_Rectangle}")
        
        
    elif choice==3:
        side=float(input("Side: "))
        area_Square=side*side
        print(f"The area is {area_Square}")
        
    elif choice==4:
        radius=float(input("Radius: "))
        area_Circle=3.14*radius*radius
        print(f"The area is {area_Circle}")
        
    elif choice==5:
        print("Program End!")
        break
    else:
        print("\nInvalid input!") 

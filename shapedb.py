from ShapeObj import *
class shapedb:
    def __init__(self):
        self.shapeList = []

    def load (self, fileName):
        try: 
            Shape.resetCount()
            infile = open(fileName,'r')
            print("Processing <<path-to-file>>...")
            # str is a list              
            str = infile.read().split("\n")
            # print(str)
            shape_count = 0
            error_count = 0 
            counter = 0
            self.shapeList = []
            for line in str:
                counter += 1
                # check if the list is empty
                if line:
                    information = line.split() # list
                    shape_name = information[0].casefold()
                    # shape matching   
                    if shape_name == "circle":
                        # if the number of information is correct(in case out of bound)
                        if len(information) == 2:
                            radius = information[1]
                            radius = int(radius)
                            if radius > 0:
                                shape = Circle(radius)
                            else:
                                print("Error: Invalid Circle on line", counter,":",line)
                                error_count += 1
                                continue
                        else:
                            print("Error: Invalid Circle on line", counter,":",line)
                            error_count += 1
                            continue
                        
                    elif shape_name == "ellipse":
                        if len(information) == 3:
                            a = information[1]
                            b = information[2]
                            a = int(a)
                            b = int(b)
                            if a > 0 and b > 0:
                                shape = Ellipse(a,b)
                            else:
                                print("Error: Invalid Ellipse on line", counter,":",line)
                                error_count += 1
                                continue
                        else:
                            print("Error: Invalid Ellipse on line", counter,":",line)
                            error_count += 1
                            continue
                        
                    elif shape_name == "rhombus":
                        if len(information) == 3:
                            d1 = information[1]
                            d2 = information[2]
                            d1 = int(d1)
                            d2 = int(d2)
                            if d1 > 0 and d2 > 0:
                                shape = Rhombus(d1,d2)
                            else:
                                print("Error: Invalid Rhombus on line", counter,":",line)
                                error_count += 1
                                continue
                        else:
                            print("Error: Invalid Rhombus on line", counter,":",line)
                            error_count += 1
                            continue
                                               
                    elif shape_name == "shape":
                        if len(information) == 1:
                            shape = Shape()
                        else:
                            print("Error: Invalid Shape on line", counter,":",line)
                            error_count += 1
                            continue

                    else:
                        error_count += 1
                        print(f"Error: Invalid shape input {shape_name} on line", counter,":",line)
                        continue

                    if shape: 
                        self.shapeList.append(shape) # save shape into the db
                        shape_count += 1 
            print(f"Processed {len(str)} row(s), {shape_count} shape(s) added, {error_count} error(s).")
            infile.close()
        except FileNotFoundError:
            print(f"Error: File {fileName} not found!")

    
    def toSet(self):
        self.shapeList = list(set(self.shapeList))
        print("TOSET operation finished!")
        # for shape in self.shapeList:
        #     shape.print()
    
    def save(self, opFName):
        try:
            opfile = open(opFName,'w') 
            
            for shape in self.shapeList:
                opfile.write(shape.getInfo().lower() + '\n')
                
            opfile.close()
        except:
            print("Error!")
    
    def print(self):
        for shape in self.shapeList:
            shape.print()

    def summary(self):
        # create a dictionary:
        count_dict = {}

        for shape in self.shapeList:
            shapeName = shape.__class__.__name__
            count_dict[shapeName] = count_dict.get(shapeName, 0) + 1
       
        #new sorted dict
        sorted_dict = dict(sorted(count_dict.items()))

        #print
        for shape in sorted_dict:
            if shape.casefold() == "shape":
                continue
            elif shape.casefold() == "rhombus":
                print(f"{shape}(es): {sorted_dict[shape]}")
            else:
                print(f"{shape}(s): {sorted_dict[shape]}")
            
        print("Shape(s):",len(self.shapeList))

    def details(self):
        for shape in self.shapeList:
            print(shape.getInfo().lower())

    def quit(self):
        exit()



print("Menu: (Please type name)")
print("1. LOAD")
print("2. TOSET")
print("3. SAVE")
print("4. PRINT")
print("5. SUMMARY")
print("6. DETAILS")
print("7. QUIT")


db = shapedb()
while True:
    option = input("Select an option: ").lower()
    if option == "load":
        fileName = input("Enter file name: ")
        db.load(fileName)
    elif option == "toset":
        db.toSet()
    elif option == "save":
        opfileName = input("Enter an output file name: ")
        db.save(opfileName)
    elif option == "print":
        db.print()
    elif option == "summary":
        db.summary()
    elif option == "details":
        db.details()
    elif option == "quit":
        db.quit()
    else:
        print("Error: You input a wrong option!")



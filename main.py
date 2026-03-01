todo_file = "to_do.txt"
while True:
    user_choice = input (
        'do you want to add a neew to_do item? (y/n) or type exit:'
    ).lower()
    if user_choice=="exit":
       print("thank you for using the to-do program")
    break
if user_choice =="y":
    new_item = input("enter your to-do item")
    file = open(todo_file,"a",encoding="utf-8")
    file.write(new_item +"\n")
    file.close()
    print("item saved")

elif user_choice=="n":
    show_list=input("do you want to list your to-do items?(y/n)").lower()
    if show_list =="y":
        try:
          file = open(todo_file ,"r",encoding="utf-8")
          lines=file.readlines()
          file.close()
          print("\nyour to-do list:")
          for line in lines:
              print("-",line.strip())

        except FileNotFoundError:
            print("not item found yet")

else:
    print("wrong input,try again")
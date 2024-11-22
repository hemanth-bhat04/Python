def demonstrate_break_continue_pass():
    print("Demonstrating 'break':")
   
    for i in range(10):
        if i == 5:
            print("Breaking the loop at i =", i)
            break  
        print(i)

    print("\nDemonstrating 'continue':")
  
    for i in range(10):
        if i == 5:
            print("Skipping iteration at i =", i)
            continue  
        print(i)

    print("\nDemonstrating 'pass':")
    
    for i in range(10):
        if i == 5:
            print("Doing nothing at i =", i)
            pass  
        else:
            print(i)


demonstrate_break_continue_pass()

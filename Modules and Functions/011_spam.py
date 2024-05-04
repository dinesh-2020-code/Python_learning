def spam1():

    def spam2():

        def spam3():
            z = " even"
            z += y
            print("in spam3, locals are {}".format(locals()))
            return z
        
        y = " more " + x  # y must exist before spam3 is called
        y += spam3()      # do not combine these assignments
        print("in spam2, locals are {}".format(locals()))
        return y
    
    x = "spam" # x must exist before spam2() is called
    x += spam2()  # do not combine these assignments
    print("in spam1, locals are {}".format(locals()))
    return x

print(spam1())
print(locals())
print(globals())
'''
    -> Variables defined in the inner scope are not accessible to the outer scope, but vice-versa is true.
    i.e., inner scope has access to the variables defined in the outer scope.
'''

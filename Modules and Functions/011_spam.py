def spam1():

    def spam2():

        def spam3():
            z = " even more spam"
            print("in spam3, locals are {}".format(locals()))
            return z
        
        y = " more spam"
        y += spam3()
        print("in spam2, locals are {}".format(locals()))
        return y
    
    x = "spam"
    x += spam2()
    print("in spam1, locals are {}".format(locals()))
    return x

print(spam1())

'''
    -> Variables defined in the inner scope are not accessible to the outer scope, but vice-versa is true.
    i.e., inner scope has access to the variables defined in the outer scope.
'''

def normal_function(function, *arguments):
    for element in arguments:
        print("2 times {} is{:20.2f}".format(element, function(element)))

normal_function(lambda element: element * 2, *[1,2,3])
def f(*args, **kwargs):
    # print("Positinal:", args)
    print("Name:", kwargs)

# f(100, 50, 25, 5) # Positinal
f(galleons=45, sickles=67, knuts=4)
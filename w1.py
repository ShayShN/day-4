# #1
# def start_f(func):
#     def s_f():
#         print("start Function") 
#         func()
#         print("End Function")
#     return s_f

# @start_f
# def name():
#    print("midlle")
   
# name() 

# #2
# import time

# def timing_run(func):
#     def times():
#         start = time.time()
#         func()
#         end = time.time()
#         print(end - start )
#     return times

# @timing_run
# def runs():
#     for i in range(1000000):
#         print(i,end=" ")

# runs()
    
#3
def logging_arguments(func):
    def print_arguments(*args):
        print(*args)
        func()
        print("end!")
    return print_arguments

@logging_arguments
def starting(*args):
    print("0k")

starting("shay","shay","nechmad","nechmad")
        
# #4
# def uppercase(func):
#     def make_upper(name):
#         if isinstance(name, str) == True:
#             return func(name).upper()
#         else:
#             return "not string!!!"
#     return make_upper

# @uppercase
# def begain(name):
#     return name
    
# print(begain("shay"))    

#5
# def count_calls(func):
#     counter = 0
#     def wraper():
#         nonlocal counter
#         func()
#         counter +=1
#         print(counter)
#     return wraper

# @count_calls
# def starting():
#     print("starting counter!!!")
    
# starting()
# starting()
# starting() 
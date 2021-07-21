# Bad Method
# Does not help on larger code lots to see where the error exists
def bad_method():
    try:
        sqrt = 0**-1
    except Exception as e:
        print(e)

bad_method()



# Better Method
# traceback provides more visibility on where & why your error occurred
import traceback

def better_method():
    try:
        sqrt = 0**-1
    except Exception:
        print(traceback.print_exc())

better_method()

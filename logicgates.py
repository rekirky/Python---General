# Define logic gates so they can be used to resolve circuit diagrams

def and_gate(*args):
    if all(args) == True:
        return True
    else:
        return False

def not_gate(a):
    if a == True:
        return False
    else:
        return True
def or_gate(*args):
    if any(args) == True:
        return True
    else:
        return False


A = True
B = False
C = True


F = or_gate(
not_gate(or_gate(not_gate(A),not_gate(B))),
not_gate(or_gate(not_gate(C),not_gate(B))),
not_gate(or_gate(C,A)))

print(F)

price = 10
rating = 4.9
course_name = 'Python course for beginners'
is_published = True

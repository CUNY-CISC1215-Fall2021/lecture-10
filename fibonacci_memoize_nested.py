# This implementation of the recursive Fibonacci sequence improves the
# example we completed in class.
#
# The problem with the class version was that we maintained a dictionary
# outside of a recursive function, where it can be accessed and modified
# by anyone. It is often problematic to keep variables in a global scope.
#
# This alternate version improves the situation by using nested functions,
# a concept we have not discussed yet. It works by defining the recursive
# Fibonacci function within a larger wrapper function. The wrapper function
# maintains a private "answers" dictionary that only lasts as long as we
# are calculating a Fibonacci number.

def fibonacci(n):
    # A dictionary for storing answers as we compute them
    # (memoization)
    answers = {0: 1, 1: 1}

    # Nested function: Recursively calculate a Fibonacci number.
    def do_fibonacci(n):
        # Have we calculated this number already? If so, exit.
        if n in answers:
            return answers[n]
        
        # Recursive case
        answer = do_fibonacci(n-1)+do_fibonacci(n-2)

        # Save the answer before returning it!
        answers[n] = answer
        
        return answer
    
    return do_fibonacci(n)

print(fibonacci(500))
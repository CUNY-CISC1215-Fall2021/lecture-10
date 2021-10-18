# A dictionary for storing recursive solutions as we compute them
# (memoization)
answers = {0: 1, 1: 1}

def fibonacci(n):
    # Have we calculated this number already? If so, exit.
    if n in answers:
        return answers[n]
    
    # Recursive case
    answer = fibonacci(n-1)+fibonacci(n-2)

    # Save the answer before returning it!
    answers[n] = answer
    return answer

print(fibonacci(500))
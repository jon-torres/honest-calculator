# Global variables
msg_ = [
    "Are you sure? It is only one digit! (y / n):" + "\n",  # msg_[0]
    "Don't be silly! It's just one number! Add to the memory? (y / n):"
    + "\n",  # msg_[1]
    "Last chance! Do you really want to embarrass yourself? (y / n):" + "\n",  # msg_[2]
    " ... lazy",  # msg_[3]
    " ... very lazy",  # msg_[4]
    " ... very, very lazy",  # msg_[5]
    "You are",  # msg_[-1]
]
memory = 0.0

# Functions

# Returns the argument if it has only one digit of type int
def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


#  Checks for one digit values and prints a message
def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_[3]
    if (float(v1) == 1 or float(v2) == 1) and (v3 == "*"):
        msg += msg_[4]
    if (float(v1) == 0 or float(v2) == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_[5]
    if msg != "":
        msg = msg_[-1] + msg
        print(msg)


# Main code

while True:
    try:
        # The expected input are equations with the following pattern
        # x operator y (e.g., 1 + 1)
        calc = input("Enter an equation" + "\n").split()
        x, oper, y = (
            memory if (calc[0] == "M") else float(calc[0]),
            calc[1],
            memory if (calc[2] == "M") else float(calc[2]),
        )

        check(x, y, oper)

        if oper == "+":
            result = x + y
        if oper == "-":
            result = x - y
        if oper == "*":
            result = x * y
        if oper == "/":
            result = x / y

        print(result)

        # It takes the input and checks it. In case "yes" and the result is one digit,
        # then it keeps asking whether the user would want to store the input.
        # After the last question, it saves the result in the memory var and exits the loop.
        answer = input("Do you want to store the result? (y / n):" + "\n")
        if answer == "y" and is_one_digit(result):
            msg_index = 0
            while True:
                answer2 = input(msg_[msg_index])
                if answer2 == "y":
                    if msg_index < 2:
                        msg_index += 1
                    elif (answer2 == "y") and (msg_index == 2):
                        memory = result
                        break
                # If the answer is "no", the memory value is not changed and it exits the loop.
                elif answer2 == "n":
                    memory = memory
                    break
        # Else, if the answer is "yes" and the result has more than one digit,
        # then it saves the result in the memory var.
        elif answer == "y" and not (is_one_digit(result)):
            memory = result

        if input("Do you want to continue calculations? (y / n):" + "\n") == "n":
            break

    except ZeroDivisionError:
        print("Yeah... division by zero. Smart move...")
    except KeyError:
        print(
            "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
        )
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")

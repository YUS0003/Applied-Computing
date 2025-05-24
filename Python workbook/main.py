def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question)
    return response

def main():
    answer = ask_yes_no("\nPlease enter y or n: ")
    print("Thanks for entering:", answer)
    input("\nPress the key to exit.")
    
main()
    
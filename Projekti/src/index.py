import services.app_logic

def main():
    program = services.app_logic.Logic()
    command = input("Practice(1) or create new wordlist(2): ")
    if command == "2":
        program.new_wordlist()
    else:
        program.initialize()

if __name__ == '__main__':
    main()

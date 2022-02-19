def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")

#No entendi esta parte
if __name__ == '__main__':
    main()

   
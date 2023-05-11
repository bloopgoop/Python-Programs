def main():
    height = get_Height()
    for i in range(height):
        draw(i + 1)
    





def get_Height():
    while(True):
        try:
            height = int(input('Height: '))
            if height > 0:
                return height
            
        except ValueError:
            print('That is not an integer!')

def draw(n):
    print('#' * n)

main()



import logging

def convert(input: str, from_base: int, to_base: int, solution: bool = False) -> str:
    valid_base = {2, 8, 10, 16}
    if from_base not in valid_base or to_base not in valid_base:
        raise Exception("[Error] Invalid base")
    
    decimal = 0
    if from_base != 10:
        dot_pos = input.find(".")
        if dot_pos == -1:
            dot_pos = len(input)
            
        index = dot_pos - 1
        map = {}
        for i in range(len(input)):
            if input[i] == ".":
                continue
            map[i] = index
            index -= 1
        logging.info(map)
        
        for key, val in map.items():
            n = 0
            if from_base == 16:
                if input[key] >= "A" and input[key] <= "F":
                    n = ord(input[key]) - 65 + 10
                elif input[key] >= "a" and input[key] <= "f":
                    n = ord(input[key]) - 97 + 10
                else:
                    n = int(input[key])
            else:
                n = int(input[key])
            
            decimal += n * pow(from_base, val)
            
            if solution:
                print("(" + str(n) + " * 2^" + str(val) + ")", end="")
                if key < len(input)-1:
                    print(" + ", end="")
            
        if solution:
            print(" = " + str(decimal))
    else:
        decimal = int(input)
    
    result = ""
    if to_base != 10:
        list = []
        while True:
            r = decimal % to_base
            
            if to_base == 16 and r > 9:
                list.append(chr(65 + r - 10))
            else:
                list.append(r)
                
            q = int(decimal / to_base)
            
            if solution:
                print(str(decimal) + "/" + str(to_base) + " = " + str(q) + " r " + str(r))
                
            if q == 0:
                break
            
            decimal = q
            
        for i in reversed(list):
            result += str(i)
    else:
        result = str(decimal)
            
    return result

def main():
    print(convert("3b4.C8", 16, 10, True))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main()
from colorama import init, Fore as F, Style as S, Back as B
import json
import time

init()

def takeInput() -> str:
    UI: str = input(f'{F.BLUE + S.BRIGHT}[?]: {S.RESET_ALL}')
    return UI

def lexingProcess(userInput: str) -> list[str] | list:
    return userInput.strip().lower().split()

def JSON_VERSION() -> str | FileNotFoundError:
    with open("../Documents/Config/version.json", "r") as file:
        versionInfo = json.load(file)
        print(f'{S.BRIGHT}{versionInfo["version"]} - {versionInfo["status"].capitalize()}{S.RESET_ALL}')

def fullAdder(A: int,  B: int, carryIn: int) -> list[int, int]:
    return [int(A) ^ int(B) ^ int(carryIn), (int(A) and int(B)) or (int(carryIn) and (int(A) ^ int(B)))] # Sum and CarryOut

def test_binary_combinations(test_cases):
    count: int = 0
    print(f"{F.YELLOW + S.BRIGHT}Testing Binary Combinations...{S.RESET_ALL}\n")
    
    for i, num1 in enumerate(test_cases):
        for num2 in test_cases[i+1:]:  # Test against all numbers after num1
            # Convert lists to strings
            A = ''.join(map(str, num1))
            B = ''.join(map(str, num2))
            bitSize = len(A)
            
            # Perform addition
            carryIn = 0
            binaryResult = []
            
            for i in range(bitSize):
                res = fullAdder(int(A[abs(i - bitSize + 1)]), int(B[abs(i - bitSize + 1)]), carryIn)
                binaryResult.append(res[0])
                carryIn = res[1]
            
            # Verify results
            expected_sum = int(A, 2) + int(B, 2)
            actual_sum = int(''.join(map(str, binaryResult[::-1])), 2)
            
            if expected_sum % (2**bitSize) == actual_sum:
                result = f"{F.GREEN}PASS{S.RESET_ALL}"
            else:
                result = f"{F.RED}FAIL{S.RESET_ALL}"

            count += 1
            print(f"{A} + {B} = {''.join(map(str, binaryResult[::-1]))} ({actual_sum}) [{result}] - {count}")
            time.sleep(0.1)  # Add a small delay for visual effect

def main() -> None:
    print(f'{F.YELLOW + S.BRIGHT}[!]{S.RESET_ALL} {S.BRIGHT}To get help write "cores | cs".{S.RESET_ALL}')
    JSON_VERSION()
    print()

    while True:
        UI: str = takeInput()
        LUI: list[str] | list = lexingProcess(UI)

        if UI.strip().lower() in ['exit', 'quit', 'q', 'e']:
            break

        elif not UI.strip().split():
            pass
        
        elif UI.strip().lower() in ['cores', 'cs']:
            print(f'{F.YELLOW + S.BRIGHT}???{S.RESET_ALL}\n')

        elif LUI[0] == 'c':
            if LUI[1][-1] != 'b':
                print(f'{F.RED + S.BRIGHT}[!]{S.RESET_ALL} {S.BRIGHT}Read the documentation. [Code: 101]{S.RESET_ALL}\n')

            else:
                if len(LUI) != 6:
                    print(f'{F.RED + S.BRIGHT}[!]{S.RESET_ALL} {S.BRIGHT}Read the documentation. [Code: 103]{S.RESET_ALL}\n')

                else:
                    LUI[1] = LUI[1][:-1]

                    if LUI[1] == '0':
                        print(f'{F.YELLOW + S.BRIGHT}Binary:{F.RESET} {0}\n{F.YELLOW}Decimal: {F.RESET}{0}\n{F.YELLOW}Carry Out: {F.RESET}{0}{S.RESET_ALL}\n')
                        return 0
                    
                    else:
                        bitSize: int = int(LUI[1])
                        A: str = str(LUI[3])
                        B: str = str(LUI[5])

                    if len(A) != bitSize or len(B) != bitSize or len(A) != len(B):
                        print(f'{F.RED + S.BRIGHT}[!]{S.RESET_ALL} {S.BRIGHT}Read the documentation. [Code: 102]{S.RESET_ALL}\n')

                    else:
                        carryIn = 0
                        binaryResult = []
                        carryOut = False
                        start_time = time.time()

                        for i in range(bitSize):
                            res = fullAdder(int(A[abs(bitSize - i + 1)]), int(B[abs(bitSize - i + 1)]), carryIn)
                            binaryResult.append(res[0])
                            carryIn = res[1]
                            if res[1]:
                                carryOut = True
                            else:
                                carryOut = False

                        print(f'{F.YELLOW + S.BRIGHT}Binary:{F.RESET} {("".join(str(x) for x in binaryResult[::-1]))}\n{F.YELLOW}Decimal: {F.RESET}{int("".join(str(x) for x in binaryResult[::-1]), 2)}\n{F.YELLOW}Carry Out: {F.RESET}{1 if carryOut else 0}{S.RESET_ALL}\n')
                        print(f'{F.YELLOW + S.BRIGHT}Time taken: {F.RESET}{time.time() - start_time:.4f} seconds{S.RESET_ALL}\n')

        elif LUI[0] == 'test':
            # Convert your test cases from string format to list of lists
            test_cases = [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 1],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 1],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 1],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 1],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 1, 0],
                [1, 0, 0, 1, 1],
                [1, 0, 1, 0, 0],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 0],
                [1, 0, 1, 1, 1],
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 1],
                [1, 1, 0, 1, 0],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 0, 0],
                [1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 1],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 1],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 1],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 1],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 1, 0],
                [1, 0, 0, 1, 1],
                [1, 0, 1, 0, 0],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 0],
                [1, 0, 1, 1, 1],
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 1],
                [1, 1, 0, 1, 0],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 0, 0],
                [1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1],
                # ... add more test cases as needed
            ]
            test_binary_combinations(test_cases)

        else:
            print(f'{F.RED + S.BRIGHT}[!]{S.RESET_ALL} {S.BRIGHT}Invalid command.{S.RESET_ALL}\n')
        
if __name__ == '__main__':
    main()

# 1h 1m 29s - Total time taken this version - 17.26 finish clock.
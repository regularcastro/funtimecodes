def division():
        numerator = 1
        prime = 23
        iter_count = 1
        digits_list = []
        for div in range (12):
            print(f'iter_count: {iter_count}')
            print(f'start numerator: {numerator}')
            if numerator <= prime:
                print(f'numerator: {numerator}')
                digits_list.append(numerator//prime)
                print(digits_list)
                numerator = numerator*10
                iter_count += 1
                print('\n')
            if numerator >= prime:
                digits_list.append(numerator//prime)
                print(digits_list)
                numerator = (numerator%prime)*10                
                iter_count += 1
                print('\n')
division()
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max_ind1 = -1
    for i in range(n):
        if ((max_ind1 == -1) or (numbers[i]> numbers[max_ind1])):
            max_ind1 = i;
    max_ind2 = -1
    for j in range(n):
        if ((j!= max_ind1) and ((max_ind2 == -1) or (numbers[j] > numbers[max_ind2]))):
            max_ind2 = j;
    max_product = numbers[max_ind1] * numbers[max_ind2]
    return max_product

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
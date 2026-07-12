import math

def pearson_correlation(x, y):
    # 1. Ensure lists are of equal length
    n = len(x)
    if n != len(y) or n == 0:
        raise ValueError("Lists must be of equal length and non-empty")

    # 2. Calculate the means
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    # 3. Calculate the numerator (sum of products of deviations)
    #    and the denominator components (sum of squared deviations)
    numerator = 0.0
    sum_sq_x = 0.0
    sum_sq_y = 0.0

    for i in range(n):
        diff_x = x[i] - mean_x
        diff_y = y[i] - mean_y
        
        numerator += (diff_x * diff_y)
        sum_sq_x += (diff_x ** 2)
        sum_sq_y += (diff_y ** 2)

    # 4. Calculate the denominator
    denominator = math.sqrt(sum_sq_x * sum_sq_y)

    # 5. Handle edge case where denominator is 0 (no variance)
    if denominator == 0:
        return 0.0

    # 6. Return the correlation coefficient
    return numerator / denominator
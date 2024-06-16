import numpy as np

def calculate(numbers):
    if len(numbers)!= 9:
        raise ValueError("La lista debe contener nueve números")

    matrix = np.array(numbers).reshape(3, 3)

    stats = {
        'mean': [matrix.mean(axis=0), matrix.mean(axis=1), matrix.flatten().mean()],
        'variance': [matrix.var(axis=0), matrix.var(axis=1), matrix.flatten().var()],
        'standard deviation': [matrix.std(axis=0), matrix.std(axis=1), matrix.flatten().std()],
        'max': [matrix.max(axis=0), matrix.max(axis=1), matrix.flatten().max()],
        'min': [matrix.min(axis=0), matrix.min(axis=1), matrix.flatten().min()],
        'sum': [matrix.sum(axis=0), matrix.sum(axis=1), matrix.sum()]
    }

    return {key: value.tolist() for key, value in stats.items()}

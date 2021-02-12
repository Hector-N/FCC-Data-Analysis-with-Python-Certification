import numpy as np


def calculate(numbers):

    if len(numbers) != 9:
        raise ValueError('List must contain nine numbers.')

    matrix = np.array(numbers, dtype='float64').reshape((3, 3))

    calculations = {}

    calculations['mean'] = [list(matrix.mean(axis=0)),
                            list(matrix.mean(axis=1)),
                            matrix.mean()]

    calculations['variance'] = [list(matrix.var(axis=0)),
                                list(matrix.var(axis=1)),
                                matrix.var()]

    calculations['standard deviation'] = [list(matrix.std(axis=0)),
                                          list(matrix.std(axis=1)),
                                          matrix.std()]

    calculations['min'] = [list(matrix.min(axis=0)),
                           list(matrix.min(axis=1)),
                           matrix.min()]

    calculations['max'] = [list(matrix.max(axis=0)),
                           list(matrix.max(axis=1)),
                           matrix.max()]

    calculations['sum'] = [list(matrix.sum(axis=0)),
                           list(matrix.sum(axis=1)),
                           matrix.sum()]

    return calculations

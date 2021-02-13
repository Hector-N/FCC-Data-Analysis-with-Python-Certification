import numpy as np
import unicodedata


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

def theory():
    std_sign = 'σ'
    std_sign_name = unicodedata.name(std_sign)
    text = (f"Deviation means 'how far from the normal'. \n"
            f"The Standard Deviation is a measure of how spread out numbers are. \n"
            f"Its symbol is 'σ' - '{std_sign_name}'\n"
            f"formula: the square root of the Variance.\n"
            f"Variance - the average of the squared differences from the Mean. \n"
            f"Mean - the simple average. \n")
    print(text)

import numpy as np

def generate_matrix(rows, cols, matrix_type='zeros'):
    match matrix_type:
        case 'zeros':
            return np.zeros((rows, cols), dtype=int)
        case 'ones':
            return np.ones((rows, cols), dtype=int)
        case 'identity':
            return np.eye(min(rows, cols))
        case 'random':
            return np.random.randint(1, 100, (rows, cols))
        case 'diagonal':
            values = np.arange(1, min(rows, cols) + 1)
            return np.diag(values)
        case 'range':
            return np.arange(rows * cols).reshape(rows, cols)

for mtype in ['zeros', 'ones', 'random', 'range', 'identity', 'diagonal']:
    mat = generate_matrix(3, 4, mtype)
    print(f"\n--- {mtype.upper()} MATRIX ({mat.shape}) ---")
    print(mat)
    print(f"Sum: {mat.sum()}, Mean: {mat.mean():.2f}")
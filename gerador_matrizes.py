import os
import random
import string

def save_matrix(rows, cols, matrix, path):
    """Saves dimensions on the first line and matrix on subsequent lines without a trailing newline."""
    with open(path, 'w') as f:
        f.write(f"{rows} {cols}\n")
        matrix_rows = [" ".join(map(str, row)) for row in matrix]
        f.write("\n".join(matrix_rows))

def gerar_e_salvar_snapshots(n_max_letters, rows=4, cols=5):
    base_dir = "matrizes"
    total_slots = rows * cols
    alphabet = list(string.ascii_uppercase)
    
    if n_max_letters >= total_slots:
        print(f"Error: {n_max_letters} letters + 1 'R' won't fit in {rows}x{cols}.")
        return

    for n in range(1, n_max_letters + 1):
        current_letters = alphabet[:n]
        folder_name = f"{n}_ponto_entrega"
        
        # Ensure the directory exists
        sub_dir = os.path.join(base_dir, folder_name)
        os.makedirs(sub_dir, exist_ok=True)
        
        # 1. Randomly pick ONE position for R out of all slots
        r_pos = random.randint(0, total_slots - 1)
        r_row, r_col = r_pos // cols, r_pos % cols
        
        # 2. Initialize matrix
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        matrix[r_row][r_col] = 'R'
        
        # 3. Place letters in remaining slots
        available_slots = [i for i in range(total_slots) if i != r_pos]
        chosen_slots = random.sample(available_slots, len(current_letters))
        
        for i, pos in enumerate(chosen_slots):
            matrix[pos // cols][pos % cols] = current_letters[i]
        
        # 4. Save the single file
        filename = f"r_{r_row}_{r_col}.txt"
        save_matrix(rows, cols, matrix, os.path.join(sub_dir, filename))

if __name__ == "__main__":
    # This will now create 19 folders, each containing exactly 1 file.
    gerar_e_salvar_snapshots(19, rows=4, cols=5)
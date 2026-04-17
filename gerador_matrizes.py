import os
import random
import string

def save_matrix(rows, cols, matrix, path):
    """Saves dimensions on the first line and matrix on subsequent lines without a trailing newline."""
    with open(path, 'w') as f:
        # Write the first line (dimensions)
        f.write(f"{rows} {cols}\n")
        
        # Format the matrix rows
        matrix_rows = [" ".join(map(str, row)) for row in matrix]
        
        # Join rows with newlines and write as a single block
        # This ensures there is NO newline at the very end of the file
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
        
        for r_pos in range(total_slots):
            r_row, r_col = r_pos // cols, r_pos % cols
            sub_dir = os.path.join(base_dir, folder_name)
            os.makedirs(sub_dir, exist_ok=True)
            
            matrix = [[0 for _ in range(cols)] for _ in range(rows)]
            matrix[r_row][r_col] = 'R'
            
            available_slots = [i for i in range(total_slots) if i != r_pos]
            chosen_slots = random.sample(available_slots, len(current_letters))
            
            for i, pos in enumerate(chosen_slots):
                matrix[pos // cols][pos % cols] = current_letters[i]
            
            filename = f"r_{r_row}_{r_col}.txt"
            save_matrix(rows, cols, matrix, os.path.join(sub_dir, filename))

if __name__ == "__main__":
    gerar_e_salvar_snapshots(19, rows=4, cols=5)
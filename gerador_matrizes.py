import os
import itertools
import string

def save_matrix(matrix, path):
    with open(path, 'w') as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")

def gerar_e_salvar_matrizes(n_max_letters, rows=4, cols=5, max_combinations=10):
    base_dir = "matrices"
    total_slots = rows * cols
    alphabet = list(string.ascii_uppercase)
    
    for n in range(1, n_max_letters + 1):
        current_letters = alphabet[:n]
        folder_name = f"{n}_element"
        
        for r_pos in range(total_slots):
            # Create path: matrices/n_element/r_x_y/
            r_row, r_col = r_pos // cols, r_pos % cols
            sub_dir = os.path.join(base_dir, folder_name, f"r_{r_row}_{r_col}")
            os.makedirs(sub_dir, exist_ok=True)
            
            # Find all available slots for letters (excluding R)
            available_slots = [i for i in range(total_slots) if i != r_pos]
            
            # Generate combinations of positions for the letters
            # We limit this because combinations grow factorially
            comb_count = 0
            for p in itertools.permutations(available_slots, len(current_letters)):
                if comb_count >= max_combinations:
                    break
                
                # Build matrix
                matrix = [[0 for _ in range(cols)] for _ in range(rows)]
                matrix[r_row][r_col] = 'R'
                
                for i, pos in enumerate(p):
                    matrix[pos // cols][pos % cols] = current_letters[i]
                
                # Save to file
                filename = f"comb_{comb_count}.txt"
                save_matrix(matrix, os.path.join(sub_dir, filename))
                comb_count += 1

if __name__ == "__main__":
    # Example: Up to 3 letters (A, B, C), limit 5 combinations per R position
    gerar_e_salvar_matrizes(3, 4, 5, max_combinations=5)
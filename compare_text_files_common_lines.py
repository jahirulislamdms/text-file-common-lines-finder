def compare_text_files(file1_path, file2_path, output_path):
    # List of common encodings to try
    encodings = ['utf-8', 'latin-1', 'ascii', 'utf-16']
    
    def read_file_with_fallback(file_path):
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    return set(file.readlines())
            except UnicodeDecodeError:
                continue
        raise UnicodeDecodeError(f"Cannot decode {file_path} with any supported encoding")

    # Read lines from both files with encoding fallback
    try:
        lines1 = read_file_with_fallback(file1_path)
        lines2 = read_file_with_fallback(file2_path)
    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(f"Failed to read files: {str(e)}")

    # Find common lines
    common_lines = lines1.intersection(lines2)
    
    # Write common lines to output file using utf-8
    with open(output_path, 'w', encoding='utf-8') as output_file:
        for line in sorted(common_lines):
            output_file.write(line)
    
    return len(common_lines)

# Example usage with raw string paths
if __name__ == "__main__":
    file1_path = r"C:\Users\mypc\Downloads\7day.txt"
    file2_path = r"C:\Users\mypc\Downloads\new1.txt"
    output_path = r"C:\Users\mypc\Downloads\common_lines.txt"
    
    try:
        common_count = compare_text_files(file1_path, file2_path, output_path)
        print(f"Found {common_count} common lines. Results written to {output_path}")
    except FileNotFoundError:
        print("Error: One or both input files not found")
    except UnicodeDecodeError as e:
        print(f"Encoding error: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

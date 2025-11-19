from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    lines: List[str] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line.rstrip("\n"))
    return lines


def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of strings into a list of json strings"""

    def process_file(text: str) -> str:
        text = text.replace("\\", "\\\\")   
        text = text.replace('"', '\\"')    
        text = text.replace("/", "\\/")    
        return text

    processed_file_list: List[str] = []
    for english, german in zip(english_file_list, german_file_list):
        english_escaped = process_file(english)
        german_escaped = process_file(german)

        json_line = f'{{"English":"{english_escaped}","German":"{german_escaped}"}}'
        processed_file_list.append(json_line)

    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, "w", encoding="utf-8") as f:
        for line in file_list:
            f.write(line + "\n")


if __name__ == "__main__":
    base_path = "./"
    german_path = base_path + "german.txt"
    english_path = base_path + "english.txt"
    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)
    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)
    write_file_list(processed_file_list, base_path + "concated.json")

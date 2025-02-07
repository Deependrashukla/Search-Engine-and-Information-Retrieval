Here’s a well-structured `README.md` file for your code. It explains the purpose of the project, how it works, and provides instructions for usage.

---

# Document Similarity Analysis Using TF-IDF and Cosine Similarity

This Python script calculates the similarity between documents in a directory using **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity**. The program processes text files, extracts important content, computes TF-IDF vectors, and determines the most similar document pairs based on their cosine similarity scores.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [How It Works](#how-it-works)
4. [Directory Structure](#directory-structure)
5. [Usage](#usage)
6. [Dependencies](#dependencies)
7. [Example Output](#example-output)
8. [Contributing](#contributing)
9. [License](#license)

---

## Overview
The goal of this project is to analyze a collection of text documents and identify the most similar document pairs. The program uses the following steps:
1. Extracts important content (titles and text) from each document.
2. Computes **TF-IDF vectors** for each document.
3. Calculates **cosine similarity** between all document pairs.
4. Outputs the top N most similar document pairs.

This approach is useful for tasks like document clustering, plagiarism detection, or information retrieval.

---

## Features
- **Document Parsing**: Extracts `<TITLE>` and `<TEXT>` tags from each document.
- **Text Preprocessing**: Filters alphanumeric words and converts them to lowercase.
- **TF-IDF Calculation**: Computes term frequency and inverse document frequency for each word.
- **Cosine Similarity**: Measures similarity between document pairs.
- **Top Similar Documents**: Displays the top N most similar document pairs.

---

## How It Works
### 1. Input Directory
The program takes a directory path as input. Each file in the directory represents a document.

### 2. Text Extraction
For each document:
- Extracts content within `<TITLE>` and `<TEXT>` tags.
- Filters out non-alphanumeric characters and converts words to lowercase.

### 3. TF-IDF Vectorization
- Computes **term frequency (TF)** for each word in a document.
- Computes **inverse document frequency (IDF)** for each word across all documents.
- Combines TF and IDF to create a normalized **TF-IDF vector** for each document.

### 4. Cosine Similarity
- Calculates the cosine similarity between all document pairs using their TF-IDF vectors.
- Normalizes the vectors to ensure consistent comparisons.

### 5. Output
The program outputs the top N most similar document pairs along with their cosine similarity scores.

---

## Directory Structure
Your project directory should look like this:

```
project-folder/
├── main.py               # Main script containing the logic
├── README.md             # This file
└── documents/            # Folder containing text files to analyze
    ├── doc1.txt
    ├── doc2.txt
    └── ...
```

Each text file in the `documents/` folder should follow this structure:
```plaintext
<TITLE>Sample Title</TITLE>
<TEXT>This is the main content of the document.</TEXT>
```

---

## Usage
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Deependrashukla/Search-Engine-and-Information-Retrieval.git
   cd Document-similarity
   ```

2. **Prepare Your Documents**:
   - Place your text files in a folder (e.g., `documents/`).
   - Ensure each file contains `<TITLE>` and `<TEXT>` tags.

3. **Run the Script**:
   ```bash
   python Document_similarity.py
   ```

4. **Input Directory Path**:
   - When prompted, enter the path to the folder containing your documents. For example:
     ```
     Enter directory path: /path/to/documents
     ```

5. **View Results**:
   - The program will display the top 50 most similar document pairs along with their cosine similarity scores.

---

## Dependencies
This script requires Python 3.x and the following libraries:
- `os`: For file and directory operations.
- `math`: For mathematical computations.
- `re`: For regular expression-based text filtering.

No additional dependencies are required.

---

## Example Output
When you run the script, the output will look like this:
```
('doc1.txt Doc No. 1', 'doc2.txt Doc No. 2') 0.87
('doc3.txt Doc No. 3', 'doc4.txt Doc No. 4') 0.85
('doc5.txt Doc No. 5', 'doc6.txt Doc No. 6') 0.82
...
```
Each line shows a pair of similar documents and their cosine similarity score (ranging from 0 to 1).

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- Inspired by common text analysis techniques like TF-IDF and cosine similarity.
- Built using Python's standard libraries for simplicity and portability.

---

Feel free to reach out if you have any questions or suggestions!

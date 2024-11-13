import os
import math
import re

# Define the directory path
directory_path = input("Enter directory path: ")
# List all files in the directory
files = os.listdir(directory_path)
doc_list = []
# Iterate through each file
for file_name in files:
    doc_list.append(file_name)
doc_dic = {}
for doc_id, file_name in enumerate(doc_list):
    doc_dic[file_name] = doc_id + 1


def read_document(folder_path, document_name):
    # Join the folder path and document name to get the full path
    full_path = os.path.join(folder_path, document_name)
    
    # Read the content of the document
    with open(full_path, 'r') as file:
        content = file.read()
        return content

def extract_important_content(content):
    # Find the index of TITLE and TEXT tags
    title_start = content.find('<TITLE>') + len('<TITLE>')
    title_end = content.find('</TITLE>')
    text_start = content.find('<TEXT>') + len('<TEXT>')
    text_end = content.find('</TEXT>')

    # Extract title and text
    title = content[title_start:title_end]
    text = content[text_start:text_end]

    # Combine title and text
    combined_content = (title + ' ' + text).strip()

    # Use regular expression to find alphanumeric words with underscores
    filtered_words = re.findall(r'\b\w+\b', combined_content)

    # Convert words to lowercase
    lowercase_filtered_words = [word.lower() for word in filtered_words]

    return lowercase_filtered_words

def compute_word_freq(combined_content):
    # Tokenize words and count frequencies
    word_freq = {}
    len_content = len(combined_content)
    for word in combined_content:
        # Increment frequency count
        if word in word_freq:
            word_freq[word] += (1/len_content)
        else:
            word_freq[word] = (1/len_content)

    return word_freq

def compute_idf(documents, folder_path):
    # Initialize a dictionary to store document frequency (DF) for each word
    word_df = {}
    total_documents = len(documents)
    for doc_name in documents.keys():
        # Read the document content
        content = read_document(folder_path, doc_name)

        # Extracted important content(removes contents don't have alphanumeric or underscore characters)
        important_content_token = extract_important_content(content)

        # Create a set to keep track of unique words in this document
        unique_words_in_doc = set(important_content_token)

        # Update word_df for unique words in this document
        for unique_word in unique_words_in_doc:
            if unique_word in word_df:
                word_df[unique_word] += 1
            else:
                word_df[unique_word] = 1

    # Calculate IDF for each word
    word_idf = {}
    for word, df in word_df.items():
        word_idf[word] = math.log(total_documents / (df))
    return word_idf

def calculate_norm(vector):
    sum_of_squares = 0
    for element in vector:
        sum_of_squares += element ** 2

    euclidean_norm = sum_of_squares ** 0.5
    return euclidean_norm

def calculate_tfidf_vector(tf_dict, idf_dict):
    tfidf_vector = {}
    
    for word, tf in tf_dict.items():
        tfidf_vector[word] = tf * idf_dict[word]

    # Normalize the TF-IDF vector
    norm = calculate_norm(tfidf_vector.values())
    if norm != 0:
        tfidf_vector = {word: value / norm for word, value in tfidf_vector.items()}

    return tfidf_vector

def create_tfidf_corpus(doc_dic):
    docs_tfidf_vector = {}
    for doc in doc_dic.keys():
        content = read_document(directory_path, doc)
        content = extract_important_content(content)
        tf_doc = compute_word_freq(content)
        idf_corpus_words = compute_idf(doc_dic, directory_path)
        tfidf_vect = calculate_tfidf_vector(tf_doc, idf_corpus_words)
        docs_tfidf_vector[doc] = tfidf_vect
    return docs_tfidf_vector

def calculate_cosine_similarity(documents_tfidf):
    # Initialize a dictionary to store cosine similarity values
    cosine_similarity_dict = {}

    # Create a list of document names
    doc_names = list(documents_tfidf.keys())

    # Compute cosine similarity for each pair of documents
    for i in range(len(doc_names)):
        for j in range(i + 1, len(doc_names)):
            doc1_name, doc2_name = doc_names[i], doc_names[j]
            doc1_tfidf, doc2_tfidf = documents_tfidf[doc1_name], documents_tfidf[doc2_name]

            dot_product = sum(doc1_tfidf[word] * doc2_tfidf.get(word, 0.0) for word in doc1_tfidf.keys())

            # Computeing norms (magnitudes)
            norm_doc1 = calculate_norm(doc1_tfidf.values())
            norm_doc2 = calculate_norm(doc2_tfidf.values())

            # Calculate cosine similarity
            cosine_similarity = dot_product / (norm_doc1 * norm_doc2)

            # Store the result in the dictionary
            cosine_similarity_dict[f"{doc1_name} Doc No. {doc_dic[doc1_name]}", f"{doc2_name} Doc No. {doc_dic[doc2_name]}"] = cosine_similarity
    return cosine_similarity_dict

def top_similar_documents(num_documents):
    docs_tfidf_vect = create_tfidf_corpus(doc_dic)
    cosine_similarity = calculate_cosine_similarity(docs_tfidf_vect)
    sorted_list = sorted(cosine_similarity.items(), key=lambda item: item[1], reverse=True)
    for i in sorted_list[:num_documents]:
        print(i)
top_similar_documents(50)
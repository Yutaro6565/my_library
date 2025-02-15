def cosine_similarity(vec_a, vec_b):
    a = np.array(vec_a)
    b = np.array(vec_b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def get_file_hash(content):
    """テキスト内容からハッシュ値を生成する"""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def read_existing_embeddings(output_file):
    """既存の vector.csv からファイルパスとハッシュの辞書を作成する"""
    existing_data = {}
    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_data[row["filepath"]] = row.get("hash", "")
    return existing_data

def write_embeddings_to_csv(output_file, embeddings):
    """埋め込み結果を CSV に書き込む"""
    with open(output_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["filepath", "hash", "embedding"])
        for filepath, (file_hash, embedding_vector) in embeddings.items():
            writer.writerow([filepath, file_hash, str(embedding_vector)])


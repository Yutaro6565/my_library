import markdown
from langchain.text_splitter import RecursiveCharacterTextSplitter
import yaml
import re

#1. Front Matter抽出
def extract_front_matter(md_text):
    front_matter_match = re.match(r'---\n(.*?)\n---', md_text, re.DOTALL)
    if front_matter_match:
        front_matter = yaml.safe_load(front_matter_match.group(1))
        md_body = md_text[front_matter_match.end():]
    else:
        front_matter = {}
        md_body = md_text
    return front_matter, md_body


#2. Markdown階層分割
def split_markdown_by_headers(md_body):
    sections = re.split(r'(#+ .+)', md_body)  # 見出しで分割
    chunks = []
    current_chunk = ""
    for part in sections:
        if part.startswith("#"):
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = part
        else:
            current_chunk += part
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

#3. トークン数でさらに分割
def chunk_with_token_limit(chunks, max_tokens=512):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=max_tokens,
        chunk_overlap=50,
        separators=["\n\n", "\n", " "]
    )
    final_chunks = []
    for chunk in chunks:
        final_chunks.extend(text_splitter.split_text(chunk))
    return final_chunks

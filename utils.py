import random

def chunk_list(lst, n):
    """Split list into n nearly equal chunks"""
    k, m = divmod(len(lst), n)
    return [lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]

def random_question(topic):
    return f"What is the key concept of {topic}?"

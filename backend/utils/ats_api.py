from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_scores(resume, jd):
    resume_emb = model.encode(resume, convert_to_tensor=True)
    jd_emb = model.encode(jd, convert_to_tensor=True)

    semantic_score = float(util.pytorch_cos_sim(resume_emb, jd_emb)[0][0])

    resume_words = set(resume.lower().split())
    jd_words = set(jd.lower().split())

    keyword_overlap = len(jd_words.intersection(resume_words))
    keyword_score = keyword_overlap / max(len(jd_words), 1)

    return {
        "semantic_score": round(semantic_score, 3),
        "keyword_score": round(keyword_score, 3),
        "final_score": round(0.6*semantic_score + 0.4*keyword_score, 3)
    }

from firebase_admin import firestore

db = firestore.client()

class BaseModel:
    """Simple Firestore document wrapper."""
    collection = ""  # Override in subclass

    @classmethod
    def get(cls, doc_id: str):
        doc = db.collection(cls.collection).document(doc_id).get()
        return doc.to_dict() if doc.exists else None

    @classmethod
    def create(cls, doc_id: str, data: dict):
        db.collection(cls.collection).document(doc_id).set(data)
        return data

    @classmethod
    def update(cls, doc_id: str, data: dict):
        db.collection(cls.collection).document(doc_id).update(data)

    @classmethod
    def delete(cls, doc_id: str):
        db.collection(cls.collection).document(doc_id).delete()

    @classmethod
    def list_all(cls):
        docs = db.collection(cls.collection).stream()
        return [{"id": d.id, **d.to_dict()} for d in docs]

# patients/utils.py

import hashlib

def create_blockchain_record(patient_id, diagnosis, visit_date, analysis_results, previous_hash=""):
    record = f'{patient_id}{diagnosis}{visit_date}{analysis_results}{previous_hash}'
    return hashlib.sha256(record.encode('utf-8')).hexdigest()
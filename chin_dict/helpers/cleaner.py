def clean_db_res(db_res):
    if '[' in db_res.pinyin:
        setattr(db_res, 'pinyin', db_res.pinyin[1:-1])
    if isinstance(db_res.meaning, str):
        setattr(db_res, 'meaning', db_res.meaning.strip('/').split('/'))
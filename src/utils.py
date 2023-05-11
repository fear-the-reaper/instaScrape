from db import insert_db

def get_shortcode(url):
    splited_url = url.split("/")
    index = -2 if url.endswith("/") else -1
    return splited_url[index]
    

def insert_comment(conn, data):
    INSERT_COMMENT_QUERY = "INSERT INTO instagram_comments (post_url, username, comment, is_complaint, sentiment) VALUES (%s, %s, %s, %s, %s)"
    value = (
        data["post_url"],
        data["username"],
        data["comment"],
        data["is_complaint"],
        data["sentiment"]
    )
    inserted = insert_db(conn, INSERT_COMMENT_QUERY, value)
    print(f"comment insert {inserted}")
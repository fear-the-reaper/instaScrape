def get_shortcode(url):
    splited_url = url.split("/")
    index = -2 if url.endswith("/") else -1
    return splited_url[index]
    
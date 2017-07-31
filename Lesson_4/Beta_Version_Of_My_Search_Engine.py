def get_page(page):
    try:
        import urllib
        return urllib.urlopen(page).read()
    except:
        return ""

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and max_pages > len(crawled):
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

def record_user_click(index,keyword,url):
    urls_list_result = lookup(index,keyword)
    if urls_list_result:
        for entry in urls_list_result:
            if url == entry[0]:
                entry[1] += 1

def add_to_index(index, keyword, url):
    for entry in index:    # index = [[keyword, [[url, count], [url,count], [url, count],...]], ...]
        if entry[0] == keyword:
            for links in entry[1]:
                if links[0] == url:
                    return
            entry[1].append([url, 0])
            return
    # not found, add new keyword to index
    index.append([keyword,[[url,0]]])

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def lookup(index, keyword):    # The Customer types in the keyword they want to lookup (search for)
    for entry in index:
        if entry[0] == keyword:
            return entry[1]    # The lookup function outputs the links (if any) associated with the entered keyword.
    return None

seed, max_pages = 'https://xkcd.com/about/', 100
print crawl_web(seed, max_pages)
index = crawl_web(seed, max_pages)
print lookup(index, 'the')

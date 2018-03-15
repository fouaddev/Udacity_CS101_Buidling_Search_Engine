def compute_ranks(graph):
    d = 0.8  # damping factor
    numloops = 10

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages

            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))

            newranks[page] = newrank
        ranks = newranks
    return ranks

def crawl_web(seed):  # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)

            graph[page] = outlinks

            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

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

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
    return words

def record_user_click(index,keyword,url):
    urls_list_result = lookup(index,keyword)
    if urls_list_result:
        for entry in urls_list_result:
            if url == entry[0]:
                entry[1] += 1

def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

print 'Note: Before you enter your URL address, please make sure to enter a URL that does not lead to unlimited back links'
print 'which will never finish and return the results.'
print 'For testing purposes, use this URL address "https://udacity.github.io/cs101x/urank/"'
print 'It links to limited amount of Web Pages, therefor the scraping process finishes and returns with results.'
link = str(input('Enter your URL between double quotes here: '))
seed = link
index, graph = crawl_web('https://udacity.github.io/cs101x/urank/')
ranks = compute_ranks(graph)

print ' '

print 'Here is all the data scrapped as an Index list that contains all content words and Web Pages found.'
print 'Each word is grouped with all links that contain it:'

print crawl_web('https://udacity.github.io/cs101x/urank/')

print ' '

print 'Note: Before you enter a keyword, please make sure to enter a simple keyword like "the" or "buy" or "more"...etc,'
print 'due to limited data scraped.'
key = str(input('Enter your keyword between quotes here: '))
print 'Here is a list of all the scraped links that contain the keyword "' + key + '":'
print lookup(index,key)

print ' '

print 'Here is a list of all links scrapped with their ranking indicator, based on their popularity:'
print ranks

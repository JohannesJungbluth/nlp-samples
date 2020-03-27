import feedparser


class RSSFeedReader:

    def __init__(self, rss_feed_url):
        self.rss_feed_url = rss_feed_url
        self.feed = None
        self.update()

    def update(self):
        self.feed = feedparser.parse(self.rss_feed_url)

    def get_tags(self):
        tag_terms = set()
        for tags in [entry.tags for entry in self.feed.entries]:
            tag_terms = tag_terms.union({tag.term for tag in tags})
        return tag_terms

    def get_titles(self):
        return [entry.title for entry in self.feed.entries]

    def get_contents(self):
        contents = []
        for entry_contents in [entry.content for entry in self.feed.entries]:
            contents.extend([content.value for content in entry_contents])
        return contents


if __name__ == "__main__":
    rss_feed_reader = RSSFeedReader("https://www.reddit.com/r/worldnews/.rss")

    tags = rss_feed_reader.get_tags()
    for tag in tags:
        print(tag)

    titles = rss_feed_reader.get_titles()
    for title in titles:
        print(title)

    contents = rss_feed_reader.get_contents()
    for content in contents:
        print(content)

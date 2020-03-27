from rss_feed_reader import RSSFeedReader
from text_pre_processing import TextPreProcessor

if __name__ == "__main__":
    rss_feed_reader = RSSFeedReader("https://www.reddit.com/r/worldnews/.rss")
    titles = rss_feed_reader.get_titles()

    text_pre_processor = TextPreProcessor()
    pre_processed_titles = [text_pre_processor.pre_process_text(title) for title in titles]

    for pre_processed_title in pre_processed_titles:
        print(pre_processed_title)

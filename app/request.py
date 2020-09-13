from newsapi import NewsApiClient


class NewsRequests:
    news = NewsApiClient(api_key='a493e30f11b147d0ba67b15ca60c5e4c')

    def get_top_headlines(self, **kwargs):
        news = self.news.get_top_headlines(**kwargs)

        return news

# Scrapy settings for e21job project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'e21job'

SPIDER_MODULES = ['e21job.spiders']
NEWSPIDER_MODULE = 'e21job.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'e21job (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'e21job.pipelines.E21JobPipeline': 300,
}

LOG_LEVEL = 'INFO'
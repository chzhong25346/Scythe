# Scythe

Scythe is a python Scrapy script to fetch multiple data sources local database. Also it makes analysis reports that mark down important market signals and saves into tables. Lastly it simulates trading based on these signals.

## Getting Started

Python3.5 or higher version and Pandas, Numpy, SQLAlchemy and ect.
A loca/remote Mysql is required and db "learning" are created.
Environment varibles to enter in OS:
```
DB_USER="DB_USER"
DB_PASS="DB_PASSWORD"
DB_HOST="localhost"
DB_PORT="3306"
EMAIL_USER="SENDER_GMAIL"
EMAIL_PASS="SENDER_GMAIL_PWD"
EMAIL_TO="MYDOG@GMAIL.COM,MYCAT@GMAIL.COM"
AV_KEY="ALPHAVANTAGE_KEY"
```

### Prerequisites

What things you need to install the software and how to install them

```
python3.5+
pandas, numpy, sqlalchemy, yaml, logger and etc.
mysql installed separately
```


### Usage
scrapy crawl list
scrapy crawl XXX


## Authors

* **Colin Zhong** - *Initial work* - [Git Page](https://github.com/chzhong25346)

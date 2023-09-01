import gzip

with gzip.open('/Users/mac/Downloads/calendar.csv.gz', 'rt', newline='') as csv_file:
    csv_data = csv_file.read()
    with open('/Users/mac/Documents/github/analytics-portfolio/projects/airbnb/raw-data/calendar.csv', 'wt') as out_file:
         out_file.write(csv_data)

with gzip.open('/Users/mac/Downloads/listings.csv.gz', 'rt', newline='') as csv_file:
    csv_data = csv_file.read()
    with open('/Users/mac/Documents/github/analytics-portfolio/projects/airbnb/raw-data/listings.csv', 'wt') as out_file:
         out_file.write(csv_data)

with gzip.open('/Users/mac/Downloads/reviews.csv.gz', 'rt', newline='') as csv_file:
    csv_data = csv_file.read()
    with open('/Users/mac/Documents/github/analytics-portfolio/projects/airbnb/raw-data/reviews.csv', 'wt') as out_file:
         out_file.write(csv_data)
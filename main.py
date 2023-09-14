import os
import urllib.request
from datetime import datetime, timedelta

# Constants
LOG_URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_LOG_FILE = 'http_access_log.txt'
SIX_MONTHS_IN_DAYS = 183

def download_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def count_requests(filename):
    total_requests = 0
    last_six_months_requests = 0

    current_date = datetime.strptime('11/Oct/1995', '%d/%b/%Y')
    six_months_ago = current_date - timedelta(days=SIX_MONTHS_IN_DAYS)
    
    with open(filename, 'r') as file:
        for line in file:
            total_requests += 1
            
            # Extract date from the log entry
            try:
                date_str = line.split('[')[1].split(']')[0].split(':')[0]
                date_obj = datetime.strptime(date_str, '%d/%b/%Y')
                
                if six_months_ago <= date_obj <= current_date:
                    last_six_months_requests += 1
            

                week_key = dat_obj.strftime('%Y-%U')
                weekly_requests[week_key] = weekly_request.get(week_key, 0) + 1

                month_key = date_obj.strftime('%Y-%m')
                month_request[month_key] = monthly_requests.get(month_key, 0) + 1
            
                file = line.split('"')[1].split()[1]
                file_counts[file] = file_count.get(file, 0) + 1

            except IndexError:
                continue
    return total_request, last_six_months_request, daily_requests, weekly_requests, monthly_requests, file_counts

def split_log_by_month(filename):
        with open(filename, 'r') as file:
            for line in file:
                try:
                    date_str = line.split('[')[1].split(']')[0].split(':')[0]
                    date_obj = datetime.strptime(date_str, '%d/%b/%Y')
                    month = date_obj.strftime('%Y-%m')
                    with open(f'long_{month}.txt', 'a') as month_file:
                        month_file.write(line)
                expect IndexError:
                    continue
def main():
    # Check if log file exists
    if not os.path.exists(LOCAL_LOG_FILE):
        print("Downloading log file...")
        download_file(LOG_URL, LOCAL_LOG_FILE)

    total, last_six_months, daily_requests, weekly_requests, monthly_requests, file_counts = count_requests(LOCAL_LOG_FILE)

    print(f"Total requests in the last 6 months from October 11, 1995: {last_six_months}")
    print(f"Total requests in the log period: {total}")

    # calculate and print requests per day
    print("\nRequests per Day:")
    for day, count in daily_requests.items():
        print(f"{day}: {count} requests")

    # calculate and print requests per week
    print("\nRequests per Week:")
    for week, count in weekly_requests.items():
        print(f"Week {week}: {count} requests")

    # calculate and print requests per month
    print("\nRequests per Month:")
    for month, count in monthly_requests.items():
        print(f"{month}: {count} requests")

if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""
12. Provide stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')

nginx_collection = client.logs.nginx

amount_of_logs = nginx_collection.count_documents({})

print(f"{amount_of_logs} logs")
print("Methods:")
for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    count = nginx_collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

status_check_count = nginx_collection.count_documents({
    "method": "GET",
    "path": "/status"
})
print(f"{status_check_count} status check")

#!/bin/env python

import os
from dotenv import load_dotenv

load_dotenv()

HOARDER_API_KEY = os.getenv('HOARDER_API_KEY')
print(HOARDER_API_KEY)

HOARDER_SERVER_ADDR = os.getenv('HOARDER_SERVER_ADDR')
print(HOARDER_SERVER_ADDR)

hoarder_all_bookmarks = os.system('hoarder bookmarks list --api-key ' + HOARDER_API_KEY + ' --server-addr ' + HOARDER_SERVER_ADDR)
print(hoarder_all_bookmarks)

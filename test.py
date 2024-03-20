#!/usr/bin/env python3
import os
from dotenv import dotenv_values
import postgres_tool
config = {
    **dotenv_values(".env")
}

db = postgres_tool.PostgresTool(config['HOST'], config['USER'], config['PORT'], config['PASSWORD'], config['DATABASE'])
print(db.get_all_table())

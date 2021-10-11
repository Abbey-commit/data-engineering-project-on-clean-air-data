import openaq

api = openaq.OpenAQ()
status, resp = api.measurements(country="NG", limit = 10000)
if status != 200:
    raise Exception("Error calling this api")
print(resp)
#     page = resp["meta"]["page"]
#     limit = resp["meta"]["limit"]
#     pages = resp["meta"]["pages"]
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     ingest_data()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

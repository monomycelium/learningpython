import urllib.parse
wiki = input()
print('[' + wiki + "](#" + urllib.parse.quote(wiki) + ')')
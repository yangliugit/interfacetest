import redis

r = redis.Redis(host='10.10.141.111', port=6379, db=0, password=None)
# r.set('name', 'liuyang')
print r.get('name')

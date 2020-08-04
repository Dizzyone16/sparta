from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta
#
moviestar = db.movies.find_one({'title': '월-E'})
# print(moviestar['star'])

# Read(조회) - 여러 값 ( _id 값은 제외하고 출력)
same_stars = list(db.movies.find({'star': moviestar['star']}, {'_id': False}))

for same_star in same_stars:
    #print(same_star['title'])
    db.movies.update_one({'star': moviestar['star']}, {'$set': {'star': 0}})
    # 똑같은 기능을 하는 다른 코드
    # db.movies.update_one({'title': same_star['title']}, {'$set': {'star': 9.41}})
# Update(업데이트) - 여러 값
# db.movies.update_one({'star': moviestar['star']}, { '$set': {'star': 0}})

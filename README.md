# note-tool

pip install git+https://github.com/Kitune2/note-tool

import note

client = note.note()

res = client.like(url,session_id)#session_idはなくてもいい
print(res)
#201
res = client.follow(session_id,user_name)user_nameはフォローの対象のアカウントのユーザーネーム
print(res)
#201

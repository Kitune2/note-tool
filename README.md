# 使い方

pip install git+https://github.com/Kitune2/note-tool



------------------------------------------------------------------------------------
import note

client = note.note()

res = client.like(url,session_id)    #session_idはなくてもいい

print(res)
#201

res = client.follow(session_id,user_name)    #user_nameはフォローの対象のアカウントのユーザーネーム

print(res)
#201

res = client.create_account("api_key","name","passwored","email")
#{"name":name,"password":password,"email":email,"session_id":new_sessionID}

------------------------------------------------------------------------------------

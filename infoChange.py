def infoC_Views(request):
	userid=request.session[user]
	ThisUser=User.Object.filter(userid=userid)
	if request.meth==['POST']:
		try:
			NewName=request.post['ChangeName']
			Newpwd=request.post['Changepwd']
			NewEmail=request.post['CHangeEmail']
			ThisUser.NewName=NewName
			ThisUser.Newpwd=Newpwd
			ThisUser.NewEmail=NewEmail
			ThisUser.save()
		except Exception as e:
			errMsg=e
		else:
			errMsg='successful!'
	return render('11-infoC',local())
{{ ThisUser.uname }}
{{ ThisUser.pwd }}
{{ ThisUser.Email }}
def Card_Library_Views(request):
	cardList=TaroLibrary.Object.filter()
	cardList=[card for card in cardList]
	# 整合url和对象
	cardList=[list(card,ToIMG(card.id)) for card in cardList]
	CardId=request.get['CardId']
	ThisCard=TaroLibrary.Object.filter(CardId=CardId)
	ThisImg='/static/img/taro'+str(CardId)+'.png'
	return render('09-taroLibrary',local())
{% for card in cardList %}
{% if card.0.id>=11 %}
	LargeAe
{% else %}
	LittleAe
{% endif %}
	{{ card.0.Cname }}
	{{ Card.0.id }}
	{{ Card.1 }}
{% endfor %}




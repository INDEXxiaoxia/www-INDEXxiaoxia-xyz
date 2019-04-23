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

def Card_Library_Views(request):

	cardList=TaroLibrary.Object.filter()
	cardList=[card for card in cardList]
	CardId=request.get['CardId']
	ThisCard=TaroLibrary.Object.filter(CardId=CardId)
	ThisImg='/static/img/taro'+str(CardId)+'.png'
	return render('09-taroLibrary',local())






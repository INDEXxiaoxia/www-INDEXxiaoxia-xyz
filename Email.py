from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

import random

class EmailVerifaction(object):
	def __init__(self,to_addr):
		self.from_addr = '**************@**'
		self.password = '******'
		self.smtp_server = 'smtp.163.com'
		self.to_addr = to_addr
	def _format_addr(self,s):
		# 格式化邮件地址
	    name, addr = parseaddr(s)
	    return formataddr((Header(name, 'utf-8').encode(), addr))
	def main_main(self):
		VerificationCode=str(random.randint(100000,999999))
		# msg = MIMEText('正文', 'plain', 'utf-8')
		msg = MIMEText('<html><body>'+
			'<p>↓↓↓您的验证码为↓↓↓</p>' +
			'<h1>'+VerificationCode+'</h1>' +
			'<p>↑↑↑上面是您的验证码↑↑↑</p>' +
		    '<p>如果不是您本人操作请无视此邮件！</p>' +
		    '<p>send by <a href="www.INDEXxiaoxia.xyz">幸福的活下去吧</a></p>' +
		    '</body></html>', 'html', 'utf-8')
		msg['From'] = self._format_addr('www.INDEXxiaoxia.xyz <%s>' % self.from_addr)
		msg['To'] = self._format_addr('用户 <%s>' % self.to_addr)
		msg['Subject'] = Header('来自茵夏的验证码~', 'utf-8').encode()

		server = smtplib.SMTP(self.smtp_server, 25)
		server.set_debuglevel(1)
		server.login(self.from_addr, self.password)
		server.sendmail(self.from_addr, [self.to_addr], msg.as_string())
		server.quit()

if __name__=="__main__":
	Ver=EmailVerifaction('*******@****')
	Ver.main_main()
# ====================================


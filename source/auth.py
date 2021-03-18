import requests
from lxml import html
import logging
from secrets import secrets
from selenium import webdriver
import os

log = logging.getLogger(__name__)

class Auth:

	def loginAuto(self):
		loginLink = 'https://www.chess.com/login_and_go?returnUrl=https%3A%2F%2Fwww.chess.com%2F'

		payload = {
			'_username': secrets.USERNAME,
			'_password': secrets.PASSWORD
		}

		with requests.Session() as s:

			responseGet = s.get(loginLink)
			loginPage = html.fromstring(responseGet.content)
			actionLink = self._getFullActionLink(loginPage)
			hiddenInputs = self._getHiddenInputTags(loginPage)

			payload.update(hiddenInputs)

			responsePost = s.post(actionLink, data=payload, allow_redirects=False)

			with open('page.html', 'wb') as f:
				f.write(responsePost.content)

			webbrowser.open_new_tab(os.path.realpath(f.name))

			cookies = responsePost.cookies
			# log.debug(cookies)

			for key, value in responsePost.headers.items():
				log.debug(key+'\n')

			# redirectURL = responsePost.headers
			# log.debug('REDIRECTURL: '+ str(redirectURL))

			return redirectURL, cookies


	def _getFullActionLink(self, root):
		"""
		Gets the action link of a form given a root (Htmletree or HtmlElement). Used in getInitialAuthCodeAuto
		"""
		loginForm = root.cssselect('.authentication-login-form')
		log.debug('Login Form:' + str(loginForm))
		loginPostLink = loginForm[0].action
		return loginPostLink #only one form, but it is in list format. I want it in string format

	def _getHiddenInputTags(self, root):
		"""
		Gets all input tags of a root so the form can be properly submitted. Used in getInitialAuthCodeAuto
		"""
		loginForm = root.cssselect('.authentication-login-form')
		hiddenInputs = {}
		for inputTag in loginForm[0].iter('input'):
			if inputTag.attrib['type'] == 'hidden' and 'name' in inputTag.attrib.keys():
				# print(inputTag.attrib)
				hiddenInputs.update({inputTag.attrib['name']: inputTag.attrib['value']})

		return hiddenInputs

	def loginUI(self):

		loginLink = 'https://www.chess.com/login_and_go?returnUrl=https%3A%2F%2Fwww.chess.com%2F'

		driver = webdriver.Chrome('../resources/chromedriver.exe')
		driver.get(loginLink)
		userField = driver.find_element_by_id('username')
		passField = driver.find_element_by_id('password')
		loginButton = driver.find_element_by_id('login')

		userField.send_keys(secrets.USERNAME)
		passField.send_keys(secrets.PASSWORD)
		loginButton.click()

		while True:
			pass


	def main(self):

		driver = self.loginUI()
		return driver
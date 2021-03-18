class Mode:

	def __init__(self, driver):
		self.driver = driver

	def lifeChess(self, driver, timeControl):

		liveChessLink = 'https://www.chess.com/live'
		driver.get(liveChessLink)

		timeSelectorButton = driver.find_element_by_class_name('time-selector-button')
		timeSelectorButton.click()

	def main(self, driver):
		pass

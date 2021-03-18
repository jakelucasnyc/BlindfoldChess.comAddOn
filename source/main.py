from auth import Auth
from webInterface import Interface
import logging


def main():

	logging.basicConfig(level=logging.INFO)
	log = logging.getLogger(__name__)


	authenticator = Auth()
	driver1 = authenticator.main()
	# interface = Interface(redirectURL, cookies)
	# interface.main()

if __name__ == '__main__':
	main()
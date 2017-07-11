import ConfigParser

def getConfig():
	config = ConfigParser.RawConfigParser()
	config.read('keys.ini')
	apiKey = config.get('firebase','apiKey');
	config = {
	  "apiKey": config.get('firebase','apiKey'),
	  "authDomain": config.get('firebase','authDomain'),
	  "databaseURL": config.get('firebase','databaseURL'),
	  "storageBucket": config.get('firebase','storageBucket')
	}
	return config;

def getAdminConfig():
        config = ConfigParser.RawConfigParser()
        config.read('keys.ini')
        apiKey = config.get('firebase','apiKey');
        config = {
          "apiKey": config.get('firebase','apiKey'),
          "authDomain": config.get('firebase','authDomain'),
          "databaseURL": config.get('firebase','databaseURL'),
	  "storageBucket": config.get('firebase','storageBucket'),
	  "serviceAccount": "./python-tester-service_account_credentials.json"
        }
        return config;


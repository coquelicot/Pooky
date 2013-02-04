import yaml, os

def loadConfig(fileName):

    dirPath = os.path.dirname(__file__)
    filePath = os.path.join(dirPath, fileName)

    with open(filePath, 'r') as fin:
        return yaml.load(fin)

try:
    config = loadConfig('config.yaml')
except:
    config = loadConfig('defaultConfig.yaml')

if config is None:
    config = dict()

# hardcode
version = 0.1

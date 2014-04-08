import pip

#Usage:
#installPackage('html2textile')
def installPackage(package):
    pip.main(['install', package])

from configurations.logger import MyLogger

if __name__ == '__main__':
    MyLogger.info('Information')
    MyLogger.exc('Exception')
    MyLogger.err('Error')
    MyLogger.debug('Debug')

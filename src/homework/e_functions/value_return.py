
def get_hour(epoch_seconds):
    hour = epoch_seconds // 3600
    return hour 

def get_minutes(epoch_seconds):
    minutes = epoch_seconds // 60 % 60
    return minutes 

def get_seconds(epoch_seconds):
    seconds = epoch_seconds  % 60
    return seconds 
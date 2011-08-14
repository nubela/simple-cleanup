#===============================================================================
# Cleanup for any directory.
# Removes file/folders older than the configured amount of days
#===============================================================================
import os
import time
import datetime
import shutil

# Configure me.

DIRS_TO_CLEAN = ("/home/nubela/Downloads", )
NUMBER_OF_DAYS_BEFORE_FILE_EXPIRES = 7

# Don't fuck with code below..

def cleanup():
    total_files_deleted = 0
    for dir in DIRS_TO_CLEAN:
        
        dir_list = os.listdir(dir)
        for f in dir_list:
            
            path_name = os.path.join(dir, f)
            duration_secs = time.time() - os.path.getmtime(path_name)
        
            if datetime.timedelta(seconds=duration_secs) > datetime.timedelta(days=NUMBER_OF_DAYS_BEFORE_FILE_EXPIRES):
                
                if os.path.isfile(path_name):
                    os.remove(path_name)
                    print "Deleted file: "+f
                elif os.path.isdir(path_name):
                    shutil.rmtree(path_name)
                    print "Deleted directory: : "+f
                total_files_deleted += 1
    return total_files_deleted
                    
def main():
    files_deleted = cleanup()
    print "Had a cleanup of  "+str(files_deleted)+" files/dirs."

main()

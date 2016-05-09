import os
import shutil

'''
count=0

for file in os.listdir("I:/data"):
    filename="I:/dataoutput/"+str(int(count/6))+"/"
    if not os.path.exists(filename):
        os.makedirs(filename)
    shutil.copyfile("I:/data/"+file,filename+file)
    count+=1
'''
sqlstr="""
DELIMITER $$

USE `wordembeding`$$

DROP PROCEDURE IF EXISTS `pro_insert%s`$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pro_insert%s`(word VARCHAR(50),relation VARCHAR(50),reference VARCHAR(50))
BEGIN
SET @STMT :=CONCAT("INSERT INTO t_",word," VALUES ('",word,"','",relation,"','",reference,"');");
PREPARE STMT FROM @STMT;
EXECUTE STMT;
   END$$

DELIMITER ;
"""

print (sqlstr % str(103))
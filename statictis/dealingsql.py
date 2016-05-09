#coding:utf-8
import os
import shutil
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
'''
for i in range(104,341):
    print(sqlstr % (str(i),str(i)))
    '''
'''
count=0
for filedir in os.listdir("I:/data2/"):
    print(filedir)
    for file in os.listdir("I:/data2/"+filedir+"/"):
        filename="I:/data3/"+str(int(count/11))+"/"
        if not os.path.exists(filename):
            os.makedirs(filename)
        shutil.move("I:/data2/"+filedir+"/"+file,filename+file)
        count+=1
'''
'''
count=0
for filedir in os.listdir("I:/data2/"):
    for file in os.listdir("I:/data2/"+filedir+"/"):
        dname=file.split("_")[0]
        #shutil.move("I:/data2/"+filedir+"/"+file,"I:/数据/relations/data/results_part1/"+dname+"/"+file)
        print("I:/data2/"+filedir+"/"+file,"I:/数据/relations/data/results_part1/"+dname+"/"+file)
        count+=1
        '''
sqlstr="""
CREATE TABLE IF NOT EXISTS %s (
  `reference` VARCHAR(70) DEFAULT NULL,
  `nmod` BIGINT(20) DEFAULT '0',
  `amod` BIGINT(20) DEFAULT '0',
  `nsubj` BIGINT(20) DEFAULT '0',
  `aux` BIGINT(20) DEFAULT '0',
  `advmod` BIGINT(20) DEFAULT '0',
  `cop` BIGINT(20) DEFAULT '0',
  `case` BIGINT(20) DEFAULT '0',
  `det` BIGINT(20) DEFAULT '0',
  `compound` BIGINT(20) DEFAULT '0',
  `cc` BIGINT(20) DEFAULT '0',
  `conj` BIGINT(20) DEFAULT '0',
  `acl` BIGINT(20) DEFAULT '0',
  `dobj` BIGINT(20) DEFAULT '0',
  `nsubjpass` BIGINT(20) DEFAULT '0',
  `auxpass` BIGINT(20) DEFAULT '0',
  `ref` BIGINT(20) DEFAULT '0',
  `mwe` BIGINT(20) DEFAULT '0',
  `mark` BIGINT(20) DEFAULT '0',
  `xcomp` BIGINT(20) DEFAULT '0',
  `advcl` BIGINT(20) DEFAULT '0',
  `neg` BIGINT(20) DEFAULT '0',
  `appos` BIGINT(20) DEFAULT '0',
  `ccomp` BIGINT(20) DEFAULT '0',
  `nummod` BIGINT(20) DEFAULT '0',
  `parataxis` BIGINT(20) DEFAULT '0',
  `expl` BIGINT(20) DEFAULT '0',
  `iobj` BIGINT(20) DEFAULT '0',
  `csubj` BIGINT(20) DEFAULT '0',
  `discourse` BIGINT(20) DEFAULT '0',
  `csubjpass` BIGINT(20) DEFAULT '0'
) ENGINE=INNODB DEFAULT CHARSET=utf8;

"""

tablenamelist=[]
for file in os.listdir("I:/file_word/file_word/"):
    tablenamelist.append(file.strip("\n").strip(".txt"))
wfile=open("newwordlist.txt","w")
wfilet=open("output.txt","w")
for item in tablenamelist:
    wfile.write(item+"\n")
    item="t_"+item
    print(sqlstr % item)

wfile.close()
wfilet.close()
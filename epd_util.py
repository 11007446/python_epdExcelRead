class Epd_util(object):
    # d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    BASE_SQL = {
        'epd_batchinfo':
        'INSERT INTO epd_batchinfo (batchid,batchno,batchnum,batchyear,batchym,batchgroupid,pgcount,pcount,expertcount,expertnum,batchtype,batchstate,importdate,intervalstart,intervalend) values ',
        'epd_batchstatement':
        'insert into epd_batchstatement (bsid,batchgroupid,expertid,expertname,expertsex,expertidnumber,expertaddress,expertpostnumber,expertmailbox,appraisepronum,payment,tax,remittancecharge,comment,batchtype,expertidtype,expertbirthdate,expertbanktype,expertbankaddress,expertbankbranch,expertbanknumber,bankUser,expertmobile) values ',
        'epd_pginfo':
        'insert into epd_pginfo (pgid,pgname,pgyear,pgmanager,pgcudatee,pgreviewcompletedate,pgcatanodeid,projnum,pgexpertnum,pgexpertsubmitnum,zjbatchid,batchgroupid,pgmoney,importdate,initFlag,iszj) values ',
        'epd_expertinfo':
        'insert into epd_expertinfo (expertid,expertname,expertinfoid,pgid,appraisesubmitdate,importdate) values ',
        'epd_projectinfo':
        'insert into epd_projectinfo (pid,pgid,pname,catapayment,importdate) values ',
        'epd_log':
        'insert into epd_log (logid,action,actiontime,account,accountname) values '
    }

    VALUE_SQL = {
        'epd_batchinfo':
        '(\'{0[0]}\',\'{0[1]}\',{0[2]},\'{0[3]}\',\'{0[4]}\',\'{0[5]}\',{0[6]},{0[7]},{0[8]},{0[9]},\'ZJ\',\'010\',getdate(),\'{0[10]}\',\'{0[11]} 23:59:59\' );',
        'epd_batchstatement':
        '(newid(),\'{0[0]}\',\'{0[1]}\',\'{0[2]}\',\'{0[3]}\',\'{0[4]}\',\'{0[5]}\',\'{0[6]}\',\'{0[7]}\',{0[8]},{0[9]},{0[10]},{0[11]},\'{0[12]}\',\'{0[13]}\',\'{0[14]}\',\'{0[15]}\',\'{0[16]}\',\'{0[17]}\',\'{0[18]}\',\'{0[19]}\',\'{0[20]}\');',
        'epd_pginfo':
        '(\'{0[0]}\',\'{0[1]}\',\'{0[2]}\',\'{0[3]}\',\'{0[4]}\',\'{0[5]}\',{0[6]},{0[7]},{0[8]},\'{0[9]}\',\'{0[10]}\',{0[11]},getdate(),\'0\',\'1\');',
        'epd_expertinfo':
        '(\'{0[0]}\',\'{0[1]}\',\'_\',\'{0[2]}\',\'{0[3]}\',getdate());',
        'epd_projectinfo':
        '(\'{0[0]}\',\'{0[1]}\',\'{0[2]}\',{0[3]},getdate());',
        'epd_log':
        '(\'{0[0]}\',\'{0[1]}\',getdate(),\'{0[2]}\',\'{0[3]}\');',
    }
    pass

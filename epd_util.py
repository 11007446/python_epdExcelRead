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
        '(\'\',\'\',,\'\',\'\',\'\',,,,,\'ZJ\',\'010\',getdate(),\'\',\' 23:59:59\' );',
        'epd_batchstatement':
        '',
        'epd_pginfo':
        '',
        'epd_expertinfo':
        '',
        'epd_projectinfo':
        '',
        'epd_log':
        '',
    }
    pass

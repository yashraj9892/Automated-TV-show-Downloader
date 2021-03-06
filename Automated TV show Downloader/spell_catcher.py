#!/usr/bin/python3
######### module for searching ###########
import urllib.parse as ub
import urllib as u
import requests
import time
from bs4 import BeautifulSoup

header = { 'USER_AGENT' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}

# Space optimized Python 
# implementation of LCS problem 

# Returns length of LCS for 
# X[0..m-1], Y[0..n-1] 
def LCS(X, Y): 
	
	# Find lengths of two strings 
	m = len(X) 
	n = len(Y) 

	L = [[0 for i in range(n+1)] for j in range(2)] 

	# Binary index, used to index current row and 
	# previous row. 
	bi = bool
	
	for i in range(m): 
		# Compute current binary index 
		bi = i&1

		for j in range(n+1): 
			if (i == 0 or j == 0): 
				L[bi][j] = 0

			elif (X[i] == Y[j - 1]): 
				L[bi][j] = L[1 - bi][j - 1] + 1

			else: 
				L[bi][j] = max(L[1 - bi][j], 
							L[bi][j - 1]) 

	# Last filled entry contains length of LCS 
	# for X[0..n-1] and Y[0..m-1] 
	return L[bi][n] 



def spell(show):
  show2 = show
  show="TV series "+show+" IMDB"
  show =ub.urlencode({'q': show})# results q=abc+defg replace spaces by + and append q= to the starting of the string
##  print(show)
  url = 'https://www.bing.com/search?'+show
##  print(url)
  abc= []
##  n=show.count(" ")
  for start in range(1):
      req=requests.get(url,headers=header)
      if( req.status_code == requests.codes.ok):      
          soup=BeautifulSoup(req.text,'lxml')            
          for url in soup.find_all('a'):
            if("1" == url.text):
               break
            if(url.get('href') is not None  and "www.imdb.com/title/" in url.get('href')):
              corrected=''
              for s in url.text :
                if( s!='('):
                        corrected+=s
                else :
                        break
##              print(corrected)
              abc.append(corrected)
##          print(abc)
          max_match=0
          k='a'*10000
          for i in abc:
            r=LCS(show2,i)
##            print(r,max_match)
            if(r>max_match):
               k=i
               max_match=r
            elif(len(k)>len(i) and r==max_match):
                k=i
                max_match=r
          return(k)
      else:
         pass
##          print("503")
##             print(str(url)+"\n"+str(url.text)+"\n")

print(spell('suits'))

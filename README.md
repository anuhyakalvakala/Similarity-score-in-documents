# Similarity-score-in-documents

The code compares all the uploaded files with the all other files in the document  and gives it similarity score with each document using Cosine Similarity and words and tokenized using Bag of Words by removing stop words in the text.

## The documents are loaded as below :

['john.txt', 'juma.txt', 'doc.txt', 'fatma.txt', 'doc1.txt', 'doc2.txt']

## The text of the loaded documents:

['Life is all about finding money and spending on luxury stuffs\nCoz this life is kinda short , trust '
 'Life to me is about finding money and use it on things that makes you happy\ncoz this life is kinda short '
 "Hey their I'm Anuhya life is a surprise go and enjoy"
 'Life is all about doing your best in trying to\nfind what works out for you and taking most time in\ntrying to pursue those skills '
 "Hey their I'm Anuhya life is a surprise go and enjoy"
 'Hi my name is Anuhya life is very unpredictable ^go and $enjoy every single day']
 
## The Vectorized text is as below:
 
<numpy.vectorize object at 0x1385f3d30>
['life', 'is', 'all', 'about', 'finding', 'money', 'and', 'spending', 'on', 'luxury', 'stuffs', 'coz', 'this', 'life', 'is', 'kinda', 'short', 'trust']
['life', 'is', 'all', 'about', 'finding', 'money', 'and', 'spending', 'on', 'luxury', 'stuffs', 'coz', 'this', 'life', 'is', 'kinda', 'short', 'trust']
['life', 'to', 'me', 'is', 'about', 'finding', 'money', 'and', 'use', 'it', 'on', 'things', 'that', 'makes', 'you', 'happy', 'coz', 'this', 'life', 'is', 'kinda', 'short']
['hey', 'their', 'i', 'm', 'anuhya', 'life', 'is', 'a', 'surprise', 'go', 'and', 'enjoy']
['life', 'is', 'all', 'about', 'doing', 'your', 'best', 'in', 'trying', 'to', 'find', 'what', 'works', 'out', 'for', 'you', 'and', 'taking', 'most', 'time', 'in', 'trying', 'to', 'pursue', 'those', 'skills']
['hey', 'their', 'i', 'm', 'anuhya', 'life', 'is', 'a', 'surprise', 'go', 'and', 'enjoy']
['hi', 'my', 'name', 'is', 'anuhya', 'life', 'is', 'very', 'unpredictable', 'go', 'and', 'enjoy', 'every', 'single', 'day']

## The vectorized text after removing stop words:

['life finding money spending luxury stuffs coz life kinda short trust'
 'life finding money use things makes happy coz life kinda short'
 'hey anuhya life surprise go enjoy'
 'life best trying find works taking time trying pursue skills'
 'hey anuhya life surprise go enjoy'
 'hi name anuhya life unpredictable go enjoy every single day']
 
 
 ## Below are the similarity measures of the each document with other document uploaded:
 
### Doc 1
1.0000000000000002
0.6923076923076924
0.22645540682891918
0.16012815380508716
0.22645540682891918
0.17541160386140586
### Doc 2
0.6923076923076924
1.0000000000000002
0.22645540682891918
0.16012815380508716
0.22645540682891918
0.17541160386140586
### Doc 3
0.22645540682891918
0.22645540682891918
1.0000000000000002
0.11785113019775793
1.0000000000000002
0.5163977794943223
### Doc 4
0.16012815380508716
0.16012815380508716
0.11785113019775793
1.0000000000000002
0.11785113019775793
0.09128709291752768
### Doc 5
0.22645540682891918
0.22645540682891918
1.0000000000000002
0.11785113019775793
1.0000000000000002
0.5163977794943223
### Doc 6
0.17541160386140586
0.17541160386140586
0.5163977794943223
0.09128709291752768
0.5163977794943223
0.9999999999999998

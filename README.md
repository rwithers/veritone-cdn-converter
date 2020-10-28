# Veritone CDN Converter 

This is a utility program to parse the commercials we get from the Westwood Affiliate Network.  
It is written in python and at present it takes the MP3 format and converts the file into a wav
format in a <cart-number>.<cut-number>.wav format for import into our automation system.  

## Example Command Line 

python parseSpots.py ~/directory-containing-mp3s-from-cdn-site

It should be apparent that the script takes a single parameter that is the path where the mp3 files exist. 

## Expected Console Output 
```
WW_AHNL85650000.MP3		97004.000
WW_BASP10M30BAB.MP3		97004.001
WW_EXERGEN1019A.MP3		97004.002
WW_MYCO522SCOTY.MP3		97004.003
WW_PGCN25520000.MP3		97004.004
WW_PGCN25630000.MP3		97004.005
WW_PGPO06810000.MP3		97004.006
WW_QTRA20002Y00.MP3		97004.007
WW_RADIO1015200.MP3		97004.008
WW_RADIOCSGAWM0.MP3		97004.009
WW_SMZRML30FREE.MP3		97004.010
WW_WALG27320000.MP3		97004.011
WW_XGGA79701000.MP3		97004.012
WW_XGGA79711000.MP3		97004.013
WW_XGGA92101000.MP3		97004.014
WW_903JR3480269.MP3		97005.000
WW_BASP10MBABBL.MP3		97005.001
WW_ROCK00911000.MP3		97005.002
WW_SMBB-CEOJOIN.MP3		97005.003
WW_SMZRML60FREE.MP3		97005.004
WW_SQ-60G-9292R.MP3		97005.005
```

## Resulting Files Created 

```
97004.000.wav
97004.001.wav
97004.002.wav
97004.003.wav
97004.004.wav
97004.005.wav
97004.006.wav
97004.007.wav
97004.008.wav
97004.009.wav
97004.010.wav
97004.011.wav
97004.012.wav
97004.013.wav
97004.014.wav
97005.000.wav
97005.001.wav
97005.002.wav
97005.003.wav
97005.004.wav
97005.005.wav
```

## Notes 

1. The program generates two cart numbers one for 30 second commercials and one for 60 second commercials. 
2. To change the cart numbers just modify the following variables in the script: 

``` 
code30 = '97004'
code60 = '97005'
```

## Todo 

1. Automate the retrieval of the MP3 file from the CDN site. 
2. Add the commercial id (ex. WW_XGGA79701000, WW_ROCK00911000) to WAV metadata. 
3. Keep a database of those files seen before and only download new files. 
4. Add a requirements.txt file to help with setting up the python virtual environment. 


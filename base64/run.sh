base64 run.sh > encoded.b64
base64 -d encoded.b64 > decoded.txt
diff run.sh decoded.txt

base64 decoded.txt > encoded2.b64
base64 -d encoded2.b64 > decoded2.txt
diff run.sh decoded2.txt

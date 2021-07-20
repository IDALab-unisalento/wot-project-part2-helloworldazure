Il file contenente il codice per l'invio dei dati è basicDiscovery.py
La cartella greengrasssdk contiene le librerie necessarie per utilizzare lo script.
Gli altri file sono le chiavi ed i certificati del dispositivo
Per eseguire il codice è necessario spostarsi con il terminale dentro la cartella nella quale è presente basicDiscovery.py ed immettere il seguente comando:
python basicDiscovery.py --endpoint abe6ixz2dives-ats.iot.us-east-1.amazonaws.com --rootCA root-ca-cert.pem --cert 3739f60df4.cert.pem --key 3739f60df4.private.key --thingName HelloWorld_Publisher --topic "hello/world/messaggio/trigger" 
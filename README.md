#tratando saida do https://github.com/FroydCod3r/Credential-Cool
cat creds.json |jq | grep "passw" | cut -d ":" -f 2 | sed 's/"//g' | sed 's/ //g' >> senhas.txt

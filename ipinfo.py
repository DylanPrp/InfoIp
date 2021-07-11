#!bin/bash


blanco="\033[1;37m"
moradofuerte="\033[0;35m"
rojo="\033[1;31m"
amarillo="\033[1;33m"
morado="\033[0;35m"
cyan="\033[0;36m"
azul="\033[1;34m"

clear

echo -e $cyan"                                                          "
echo "  ██▓ ███▄    █   █████▒▒█████               
▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒             
▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒             
░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░             
░██░▒██░   ▓██░░▒█░   ░ ████▓▒░             
░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░              
 ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░              
 ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒               
 ░           ░            ░ ░               
                                            
 ██▓ ██▓███                                 
▓██▒▓██░  ██▒                               
▒██▒▓██░ ██▓▒                               
░██░▒██▄█▓▒ ▒                               
░██░▒██▒ ░  ░                               
░▓  ▒▓▒░ ░  ░                               
 ▒ ░░▒ ░                                    
 ▒ ░░░                                      
 ░                                          
                                            
▓█████▄▓██   ██▓ ██▓    ▄▄▄       ███▄    █ 
▒██▀ ██▌▒██  ██▒▓██▒   ▒████▄     ██ ▀█   █ 
░██   █▌ ▒██ ██░▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█▄   ▌ ░ ▐██▓░▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▒████▓  ░ ██▒▓░░██████▒▓█   ▓██▒▒██░   ▓██░
 ▒▒▓  ▒   ██▒▒▒ ░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ░ ▒  ▒ ▓██ ░▒░ ░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░
 ░ ░  ░ ▒ ▒ ░░    ░ ░    ░   ▒      ░   ░ ░ 
   ░    ░ ░         ░  ░     ░  ░         ░ 
 ░      ░ ░                                 "
echo -e $amarillo"                               "
read -p "IP > " ip
curl -s http://ip-api.com/$ip

sleep 1
echo -e $cyan"                                 "
echo
echo -e $amarillo"                                  "
nmap $ip


echo -e $rojo
figlet sslscan
echo -e $amarillo
sslscan $ip

echo -e $rojo
figlet whatweb
whatweb $ip

echo -e $rojo
figlet davtest
echo -e $amarillo
davtest -url $ip

echo -e $rojo
figlet fierce
echo -e $amarillo
fierce --domain $ip

echo -e $rojo
figlet unicornscan
echo -e $amarillo
unicornscan $ip


echo -e $rojo
figlet dmitry
echo -e $amarillo
dmitry -winspef -o page.txt $ip

echo -e $rojo
figlet nikto
echo -e $amarillo
nikto -h $ip




echo -e $rojo
figlet dnsmap
echo -e $amarillo
dnsmap $ip

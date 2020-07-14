echo "Installation......"

mkdir /etc/Fr13nd/ && mv fr13ndbd.py /etc/Fr13nd/fr13ndbd && chmod +x /etc/Fr13nd/fr13ndbd && ln -s /etc/Fr13nd/fr13ndbd /usr/bin/fr13ndbd 
rm install.sh

echo "Installation OK..."
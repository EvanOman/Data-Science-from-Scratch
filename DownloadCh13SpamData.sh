# Make Data dir if it doesn't exist
if [ ! -d "$DIRECTORY" ]; then
	mkdir Ch13_data
fi

# download data
wget https://spamassassin.apache.org/publiccorpus/20021010_easy_ham.tar.bz2
wget https://spamassassin.apache.org/publiccorpus/20021010_hard_ham.tar.bz2
wget https://spamassassin.apache.org/publiccorpus/20021010_spam.tar.bz2

# extract data
tar -xvf 20021010_easy_ham.tar.bz2
tar -xvf 20021010_hard_ham.tar.bz2
tar -xvf 20021010_spam.tar.bz2

# move data to data folder
mv -f easy_ham ./Ch13_data
mv -f hard_ham ./Ch13_data
mv -f spam ./Ch13_data

# rm archives
rm *.tar.bz2

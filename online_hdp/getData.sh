#Download NYTIMES from UCI repository
wget -P data/ https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/docword.nytimes.txt.gz
gunzip data/docword.nytimes.txt.gz
wget -P data/ https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.nytimes.txt
dist/preprocessing UCI data/docword.nytimes.txt data/vocab.nytimes.txt data/nytimes 1500 1
rm -rf data/docword.nytimes.txt.gz data/docword.nytimes.txt data/vocab.nytimes.txt
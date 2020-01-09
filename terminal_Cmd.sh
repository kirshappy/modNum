#move files 1976 to 1982 to a new folder
for ((fname=1976;fname<=1982;fname++));do cp ${fname}*.txt_en /home/myriam/modNum/data;done

# count number of files in folder
ls|grep txt_en|wc -l
# 5913
# 5912 1977_0018* 1.txt_en duplicate

#change extension name from txt_en to txt
for fname in *.txt_en; do mv ${fname} ${fname%%.txt_en}.txt;done

#merge all files into single one
cat data/*.txt > data/allEn.txt
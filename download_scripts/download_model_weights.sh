#!/bin/bash
# These files are to be downloaded from https://nextcloud.mpi-klsb.mpg.de/index.php/s/LTWJPcRt7gsgoss
# To get the download links, do the following
#  1. Open the above link in Google Chrome
#  2. Right click > Inspect
#  3. Goto Network tab
#  4. Now download a file using UI. A new request appears in the Name column. Click on the new request.
#  5. "Headers tab > General section > Request URL" has the desired url. Copy it and put it in a curl command.

curl -o old-t-shirt_female_weights.zip "https://nextcloud.mpi-klsb.mpg.de/index.php/s/LTWJPcRt7gsgoss/download?path=%2F&files=old-t-shirt_female_weights.zip&downloadStartSecret=ufpghe4mf0r"
curl -o pant_female_weights.zip "https://nextcloud.mpi-klsb.mpg.de/index.php/s/LTWJPcRt7gsgoss/download?path=%2F&files=pant_female_weights.zip&downloadStartSecret=2l0xvaizwxj"
curl -o pant_male_weights.zip "https://nextcloud.mpi-klsb.mpg.de/index.php/s/LTWJPcRt7gsgoss/download?path=%2F&files=pant_male_weights.zip&downloadStartSecret=gx1ostcxn0u"
curl -o shirt_female_weights.zip "https://nextcloud.mpi-klsb.mpg.de/index.php/s/LTWJPcRt7gsgoss/download?path=%2F&files=shirt_female_weights.zip&downloadStartSecret=9gykf8zt11p"
curl -o shirt_male_weights.zip "https://nextcloud.mpi-klsb.mpg.de/index.php/s/LTWJPcRt7gsgoss/download?path=%2F&files=shirt_male_weights.zip&downloadStartSecret=vyta58nep7p"
curl -o short-pant_female_weights.zip "https://nextcloud.mpi-klsb.mpg.de/index.php/s/LTWJPcRt7gsgoss/download?path=%2F&files=short-pant_female_weights.zip&downloadStartSecret=8hh5n95a2ne"
curl -o short-pant_male_weights.zip "https://nextcloud.mpi-klsb.mpg.de/index.php/s/LTWJPcRt7gsgoss/download?path=%2F&files=short-pant_male_weights.zip&downloadStartSecret=wghy2m51cmf"
curl -o skirt_female_weights.zip "https://nextcloud.mpi-klsb.mpg.de/index.php/s/LTWJPcRt7gsgoss/download?path=%2F&files=skirt_female_weights.zip&downloadStartSecret=dysca7jhmv6"
curl -o t-shirt_female_weights.zip "https://nextcloud.mpi-klsb.mpg.de/index.php/s/LTWJPcRt7gsgoss/download?path=%2F&files=t-shirt_female_weights.zip&downloadStartSecret=8jfhivai0ch"
curl -o t-shirt_male_weights.zip "https://nextcloud.mpi-klsb.mpg.de/index.php/s/LTWJPcRt7gsgoss/download?path=%2F&files=t-shirt_male_weights.zip&downloadStartSecret=p3rluhxqm1"

#wget https://datasets.d2.mpi-inf.mpg.de/tailornet/old-t-shirt_female_weights.zip
#wget https://datasets.d2.mpi-inf.mpg.de/tailornet/t-shirt_male_weights.zip
#wget https://datasets.d2.mpi-inf.mpg.de/tailornet/t-shirt_female_weights.zip
#wget https://datasets.d2.mpi-inf.mpg.de/tailornet/shirt_female_weights.zip
#wget https://datasets.d2.mpi-inf.mpg.de/tailornet/shirt_male_weights.zip
